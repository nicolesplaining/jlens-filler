#!/usr/bin/env python3
"""LoRA SFT to teach a chat model to use filler dots on chained variable binding.

Each training example is the released five-shot scaffold with the target item
rendered at one dot count drawn from ``--ks`` (mixed, including k=0), and the
loss covers only the answer tokens plus the end-of-turn token. Every
``--eval-every`` steps the adapter is evaluated with the same paired sweep used
for the behavioral screen (released 50 items at all k, plus the pre-question
placement control) so training and screening produce identical tables.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
import time
from pathlib import Path
from typing import Any

import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, get_cosine_schedule_with_warmup

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))
from analyze_behavior_sweep import summarize_rows  # noqa: E402
from extract_hf import _NoDoubleBos, make_encode_messages, run_filler_length_sweep  # noqa: E402
from jlens_filler.prompts import build_messages  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", required=True)
    p.add_argument("--train-jsonl", type=Path, required=True)
    p.add_argument("--scaffold-config", type=Path, default=Path("configs/varbind_easy_dot_length_sweep.json"),
                   help="source of few_shot demonstrations and filler_type")
    p.add_argument("--eval-config", type=Path, default=Path("configs/varbind_easy_dot_length_sweep.json"))
    p.add_argument("--control-config", type=Path, default=Path("configs/varbind_pre_question_k50_control.json"))
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--ks", default="0,5,10,25,50,100")
    p.add_argument("--epochs", type=int, default=2)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--rank", type=int, default=32)
    p.add_argument("--alpha", type=int, default=64)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--grad-accum", type=int, default=4)
    p.add_argument("--warmup-steps", type=int, default=20)
    p.add_argument("--eval-every", type=int, default=100)
    p.add_argument("--max-train-items", type=int, default=0)
    p.add_argument("--eval-limit", type=int, default=0, help="evaluate only the first N items (smoke tests)")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


class SftDataset(Dataset):
    def __init__(self, items, few_shot, filler_type, ks, tokenizer, encode_messages, eot_id, seed):
        self.rows = []
        rng = random.Random(seed)
        for item in items:
            k = rng.choice(ks)
            messages = build_messages(few_shot, item, filler_type, k, task_type="variable_binding")
            prompt = encode_messages(messages, thinking_mode="chat")
            prompt_ids = tokenizer.encode(prompt, add_special_tokens=False)
            target_ids = tokenizer.encode(str(item["answer"]), add_special_tokens=False) + [eot_id]
            self.rows.append((prompt_ids, target_ids, k))

    def __len__(self): return len(self.rows)
    def __getitem__(self, i): return self.rows[i]


def collate(batch, pad_id):
    lengths = [len(p) + len(t) for p, t, _ in batch]
    width = max(lengths)
    ids = torch.full((len(batch), width), pad_id, dtype=torch.long)
    labels = torch.full((len(batch), width), -100, dtype=torch.long)
    mask = torch.zeros((len(batch), width), dtype=torch.long)
    for i, (p, t, _) in enumerate(batch):
        seq = p + t
        ids[i, : len(seq)] = torch.tensor(seq)
        labels[i, len(p) : len(seq)] = torch.tensor(t)
        mask[i, : len(seq)] = 1
    return ids, labels, mask


@torch.inference_mode()
def evaluate(model, tokenizer, encode_messages, eval_cfg, ctrl_cfg, eos_ids, out_dir: Path, tag: str, limit: int = 0) -> dict[str, Any]:
    model.eval()
    model.config.use_cache = True
    result: dict[str, Any] = {}
    for name, cfg, task in (("eval", eval_cfg, "variable_binding"), ("control", ctrl_cfg, "variable_binding_pre_filler")):
        sweep = run_filler_length_sweep(
            model=model, tokenizer=tokenizer, encode_messages=encode_messages,
            few_shot=cfg["few_shot"], examples=cfg["examples"][:limit] if limit else cfg["examples"], filler_type=cfg["filler_type"],
            filler_lengths=[int(k) for k in cfg["filler_lengths"]], task_type=task,
            top_k=5, max_new_tokens=3, eos_ids=eos_ids,
        )
        d = out_dir / f"eval-{tag}" / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "filler_length_sweep.json").write_text(json.dumps(sweep))
        summary = summarize_rows(sweep["examples"], sweep["filler_lengths"])
        (d / "behavior-summary.json").write_text(json.dumps(summary, indent=1))
        result[name] = {k: v["correct"] for k, v in summary["by_length"].items()}
        result[name + "_helped_hurt"] = {k: (v["helped_count"], v["hurt_count"]) for k, v in summary["paired_vs_k0"].items()}
    model.config.use_cache = False
    model.train()
    return result


def main() -> None:
    args = parse_args()
    torch.manual_seed(args.seed); random.seed(args.seed)
    ks = [int(k) for k in args.ks.split(",")]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    log = (args.output_dir / "train-log.jsonl").open("a")

    tokenizer = _NoDoubleBos(AutoTokenizer.from_pretrained(args.model_id))
    encode_messages = make_encode_messages(tokenizer)
    vocab = tokenizer.get_vocab()
    eot_id = vocab.get("<|im_end|>", tokenizer.eos_token_id)
    eos_ids = sorted({tokenizer.eos_token_id, eot_id})
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else eot_id

    model = AutoModelForCausalLM.from_pretrained(args.model_id, dtype=torch.bfloat16, device_map="cuda")
    model.config.use_cache = False
    model.gradient_checkpointing_enable()
    model.enable_input_require_grads()
    from peft import LoraConfig, get_peft_model
    lcfg = LoraConfig(r=args.rank, lora_alpha=args.alpha, lora_dropout=0.05, target_modules="all-linear", task_type="CAUSAL_LM")
    model = get_peft_model(model, lcfg)
    model.print_trainable_parameters()

    scaffold = json.loads(args.scaffold_config.read_text())
    eval_cfg = json.loads(args.eval_config.read_text())
    ctrl_cfg = json.loads(args.control_config.read_text())
    items = [json.loads(l) for l in args.train_jsonl.open()]
    if args.max_train_items:
        items = items[: args.max_train_items]

    # Baseline eval before any update, using the same code path.
    print("baseline eval", flush=True)
    base = evaluate(model, tokenizer, encode_messages, eval_cfg, ctrl_cfg, eos_ids, args.output_dir, "step0", args.eval_limit)
    print("step 0", json.dumps(base), flush=True)
    log.write(json.dumps({"step": 0, **base}) + "\n"); log.flush()

    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.0, betas=(0.9, 0.95))
    steps_per_epoch = math.ceil(len(items) / (args.batch_size * args.grad_accum))
    total_steps = steps_per_epoch * args.epochs
    sched = get_cosine_schedule_with_warmup(opt, args.warmup_steps, total_steps)
    print(f"{len(items)} items, {total_steps} optimizer steps", flush=True)

    step = 0
    model.train()
    for epoch in range(args.epochs):
        ds = SftDataset(items, scaffold["few_shot"], scaffold["filler_type"], ks, tokenizer, encode_messages, eot_id, seed=args.seed + epoch)
        dl = DataLoader(ds, batch_size=args.batch_size, shuffle=True, collate_fn=lambda b: collate(b, pad_id))
        running, n_micro, t0 = 0.0, 0, time.time()
        for micro, (ids, labels, mask) in enumerate(dl):
            ids, labels, mask = ids.cuda(), labels.cuda(), mask.cuda()
            out = model(input_ids=ids, attention_mask=mask, labels=labels)
            (out.loss / args.grad_accum).backward()
            running += out.loss.item(); n_micro += 1
            if (micro + 1) % args.grad_accum == 0:
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                opt.step(); sched.step(); opt.zero_grad(set_to_none=True)
                step += 1
                if step % 10 == 0:
                    print(f"epoch {epoch} step {step}/{total_steps} loss {running/n_micro:.4f} lr {sched.get_last_lr()[0]:.2e} {(time.time()-t0)/step*1 if step else 0:.1f}s/step", flush=True)
                    log.write(json.dumps({"step": step, "epoch": epoch, "loss": running / n_micro}) + "\n"); log.flush()
                    running, n_micro = 0.0, 0
                if step % args.eval_every == 0 or step == total_steps:
                    model.save_pretrained(args.output_dir / f"adapter-step{step}")
                    res = evaluate(model, tokenizer, encode_messages, eval_cfg, ctrl_cfg, eos_ids, args.output_dir, f"step{step}", args.eval_limit)
                    print(f"step {step} EVAL {json.dumps(res)}", flush=True)
                    log.write(json.dumps({"step": step, **res}) + "\n"); log.flush()
    print("TRAIN_DONE", flush=True)


if __name__ == "__main__":
    main()
