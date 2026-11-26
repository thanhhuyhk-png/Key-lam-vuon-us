import re
p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/script.draft-markers.md"
raw = open(p, encoding="utf-8").read()
tts = raw.split("## TTS SCRIPT", 1)[1]
W = lambda s: len(re.sub(r"[#*\-`>\[\]()_]", " ", s).split())
pos = 0
out = []
chunks = re.split(r"(^###.*$)", tts, flags=re.M)
out.append(("HOOK", 0))
pos = W(chunks[0])
for i in range(1, len(chunks), 2):
    title = chunks[i].lstrip("# ").strip()
    out.append((title, pos))
    pos += W(chunks[i + 1])
for t, w in out:
    s = round(w / 2.75)
    print(f"{s//60}:{s%60:02d}  {t}")
s = round(pos / 2.75)
print("END", f"{s//60}:{s%60:02d}", pos, "words")
