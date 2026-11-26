import re, difflib
SP = r"C:/Users/admin/AppData/Local/Temp/claude/D--0002-Team-A-Nam/04c08a38-0489-4e75-bd24-efec1f8005b2/scratchpad/"
a = open(SP + "tts-in.md", encoding="utf-8").read()
b = open(SP + "tts-ff.md", encoding="utf-8").read()
def sents(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+|\n+", t) if x.strip()]
sa, sb = sents(a), sents(b)
sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
n = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    n += 1
    print(f"[{tag}] -", " | ".join(sa[i1:i2])[:230])
    print(f"      +", " | ".join(sb[j1:j2])[:260])
print("changes", n, "words", len(a.split()), "->", len(b.split()))
heads_a = [x for x in a.splitlines() if x.startswith("###")]
heads_b = [x for x in b.splitlines() if x.startswith("###")]
print("headings same:", heads_a == heads_b)
nums = lambda t: sorted(re.findall(r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|\d+)\b", t.lower()))
print("number-words same:", nums(a) == nums(b))
