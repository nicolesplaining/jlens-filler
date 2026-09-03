import json, sys, re, numpy as np, torch
sys.path.insert(0, "scripts"); from analyze_dot_residuals import ridge_cv_r2
cfg = json.load(open("configs/varbind_heldout_050_149_dot_length_sweep.json")); by_id = {e["id"]: e for e in cfg["examples"]}
pat = re.compile(r"twice the number for ([a-z]+) (plus|minus) (\d+)")
def targets(ex):
    defs = dict((n, v) for n, v in ex["definitions"]); q = ex["queried_term"]; m = pat.match(defs[q]); base_name = m.group(1)
    others = [v for n, v in defs.items() if isinstance(v, int) and n != base_name]
    distractor = others[0] if others else np.nan
    # a derived distractor value (visible expression, not on the queried chain)
    return {"queried_base": float(defs[base_name]), "distractor_literal": float(distractor), "q_constant": float(ex["constant"]),
            "def_constant": float(m.group(3)), "answer": float(ex["answer"])}
print(f"{'model':9} {'position':9} {'target':19} " + " ".join(f"L{l:>2}" for l in (16, 20, 24, 26, 29, 31)) + "   best")
for tag in ("base", "dotsonly", "k0only"):
    d = torch.load(f"results/qwen3.5-9b/dot-dump/{tag}/dot_dump.pt"); R = d["resid"].float().numpy(); N, L, P, D = R.shape; K = P - 3
    T = [targets(by_id[m["id"]]) for m in d["meta"]]; keep = np.array([not np.isnan(t["distractor_literal"]) for t in T])
    for where, sel in (("dots_mean", None), ("cue", K + 1)):
        for name in ("queried_base", "distractor_literal", "q_constant", "def_constant", "answer"):
            y = np.array([t[name] for t in T])[keep]; row = []
            for l in range(L):
                X = (R[:, l, :K].mean(1) if sel is None else R[:, l, sel])[keep]
                row.append(ridge_cv_r2(X, y, np.arange(len(y)), 10.0))
            b = int(np.argmax(row)); print(f"{tag:9} {where:9} {name:19} " + " ".join(f"{row[l]:5.2f}" for l in (16, 20, 24, 26, 29, 31)) + f"   L{b} ({row[b]:.2f})")
print("n items with a distractor literal:", int(keep.sum()))
