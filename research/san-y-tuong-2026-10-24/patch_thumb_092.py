p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/thumbnail-prompts.md"
s = open(p, encoding="utf-8").read()
a1 = "a single hand holding upright a six-inch rose cutting with exactly two visible leaf buds, standing in"
b1 = "a single hand holding upright a six-inch rose cutting. The stem has EXACTLY TWO leaf buds in total, count them: two, and NO third bud anywhere on the stem; the top end of the stem is a clean flat cut with no bud at the tip. The cutting stands in"
assert a1 in s
s = s.replace(a1, b1, 1)
a2 = "with exactly two visible leaf buds along the stem. Both buds are circled with a bold red dashed ring."
b2 = "The stem has EXACTLY TWO leaf buds in total, count them: two, and NO third bud anywhere on the stem; the top end of the stem is a clean flat cut. Only these two buds are circled, each with a bold red dashed ring."
assert a2 in s
s = s.replace(a2, b2, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")
