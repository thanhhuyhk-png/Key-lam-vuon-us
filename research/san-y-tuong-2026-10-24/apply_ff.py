import re
SP = r"C:/Users/admin/AppData/Local/Temp/claude/D--0002-Team-A-Nam/04c08a38-0489-4e75-bd24-efec1f8005b2/scratchpad/"
b = open(SP + "tts-ff.md", encoding="utf-8").read()
for junk in [" Lovely.", " A neat little finding.", " It's easy, and a little satisfying.", " It's a sad sight.", " Yes, the hard part.", " Simple, and kind of fun."]:
    if junk in b:
        b = b.replace(junk, "", 1)
    else:
        print("not found:", junk)
b = b.replace("P for potato, M for mix. Six cuttings", "P for potato, M for mix. That's it. Six cuttings")
open(SP + "tts-ff2.md", "w", encoding="utf-8").write(b)

p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/script.md"
raw = open(p, encoding="utf-8").read()
head = raw.split("## TTS SCRIPT", 1)[0]
open(p, "w", encoding="utf-8").write(head + "## TTS SCRIPT\n\n" + b.strip() + "\n")
print("applied", len(b.split()), "words")
