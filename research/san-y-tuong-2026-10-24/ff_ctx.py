import re, collections
SP = r"C:/Users/admin/AppData/Local/Temp/claude/D--0002-Team-A-Nam/04c08a38-0489-4e75-bd24-efec1f8005b2/scratchpad/"
a = open(SP + "tts-in.md", encoding="utf-8").read()
b = open(SP + "tts-ff.md", encoding="utf-8").read()
sb = [x.strip() for x in re.split(r"(?<=[.!?])\s+|\n+", b) if x.strip()]
for key in ["Sorry, no magic.", "Coffee optional.", "Lovely.", "Ouch.", "We know that's a letdown.", "A neat little finding.", "It's easy, and a little satisfying.", "It's a sad sight.", "Yes, the hard part.", "Simple, and kind of fun.", "We'd love to hear it."]:
    for i, x in enumerate(sb):
        if x == key:
            print(f"... {sb[i-1][:90]} || {x} || {sb[i+1][:90] if i+1 < len(sb) else ''}")
            break
pat = r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|\d+)\b"
ca = collections.Counter(re.findall(pat, a.lower()))
cb = collections.Counter(re.findall(pat, b.lower()))
print({k: (ca[k], cb[k]) for k in set(ca) | set(cb) if ca[k] != cb[k]})
