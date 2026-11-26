import re, os, shutil
D = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/"
p = D + "script.md"
raw = open(p, encoding="utf-8").read()
head, tts = raw.split("## TTS SCRIPT", 1)
tts = tts.strip() + "\n"

# 1) compliance fix: move rooting-powder safety paragraph before the basic build, add storage line
m = re.search(r"Now, a word on rooting powder\.[^\n]*\n\n", tts)
assert m, "powder paragraph not found"
para = m.group(0)
tts = tts.replace(para, "", 1)
para = para.replace("Now, a word on rooting powder.", "Before the build, a word on rooting powder.", 1)
para = para.rstrip("\n") + " Keep the tin closed and out of reach of kids and pets.\n\n"
anchor = "Here's the basic build."
assert anchor in tts
tts = tts.replace(anchor, para + anchor, 1)

# 2) keep a markers copy (post Triple F + compliance fix) for Pha D re-checks
open(D + "script.draft-markers.md", "w", encoding="utf-8").write(head + "## TTS SCRIPT\n\n" + tts)

# 3) digits found?
print("digits:", re.findall(r"[^\s]*\d[^\s]*", re.sub(r"^###.*$", "", tts, flags=re.M)))
open(D + "tts-markers.tmp", "w", encoding="utf-8").write(tts)
