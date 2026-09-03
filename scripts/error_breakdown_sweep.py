import json, sys, collections
d = json.load(open(sys.argv[1]))
lengths = d["filler_lengths"]
print("stage keys:", sorted({k for r in d["examples"] for k in r["expected_intermediates"]}))
for k in lengths:
    cats = collections.Counter(); examples = {}
    for r in d["examples"]:
        c = r["conditions"][str(k)]
        out = c["parsed_answer"]; ans = r["expected_answer"]
        inter = {name: int(v) for name, v in r["expected_intermediates"].items()}
        ex = r["example"]
        if out is None: cat = "unparsed"
        elif out == ans: cat = "correct"
        elif out in inter.values():
            cat = "stalled@" + [n for n, v in inter.items() if v == out][0]
        elif abs(out - ans) <= 3: cat = "off_by<=3"
        else:
            # is it the result of applying the final op to a *different* definition's value?
            cat = "other"
        cats[cat] += 1
        examples.setdefault(cat, []).append((r["id"][-4:], out, ans))
    print(f"k={k:>3}", dict(sorted(cats.items(), key=lambda x: -x[1])))
    if k in (0, 50):
        for cat in ("other", "off_by<=3"):
            print("     ", cat, "sample:", examples.get(cat, [])[:6])
# consistency: does the output change with k at all?
changed = sum(len({r["conditions"][str(k)]["parsed_answer"] for k in lengths}) > 1 for r in d["examples"])
print(f"outputs vary across k in {changed}/{len(d['examples'])} examples")
# one full example to eyeball
r = d["examples"][3]
print("\nexample", r["id"], "answer", r["expected_answer"], "intermediates", r["expected_intermediates"])
for line in r["example"]["definitions"]: print("   ", line)
print("   Q:", r["example"]["question"])
print("   outputs by k:", {k: r["conditions"][str(k)]["parsed_answer"] for k in lengths})
