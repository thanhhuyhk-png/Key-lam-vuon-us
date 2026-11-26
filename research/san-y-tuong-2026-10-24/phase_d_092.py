import re, json
PATH = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/script.md"
raw = open(PATH, encoding="utf-8").read()
tts = re.search(r"## TTS SCRIPT\s*(.*)", raw, re.DOTALL).group(1)
W = lambda s: len(re.sub(r"[#*\-`>\[\]()_]", " ", s).split())
parts = re.split(r"^###\s*(M\d|Q|KẾT)\b.*$", tts, flags=re.M)
hook = parts[0]
secs = {k: v for k, v in zip(parts[1::2], parts[2::2])}
print("HOOK", W(hook), {k: W(v) for k, v in secs.items()})
body = re.sub(r"^###.*$", "", tts, flags=re.M)
total = W(body)
print("total", total, f"{total/165:.1f} min")
cfg = json.load(open(r"D:/0002-Team A Nam/channel.config.json", encoding="utf-8"))["video_length"]
print("config", cfg["target_words_min"], cfg["target_words_max"], "UNDER" if total < cfg["target_words_min"] else "OK")


def at(c):
    i = body.lower().find(c.lower())
    return round(W(body[:i]) / 2.75) if i >= 0 else -1


def f(x):
    return f"{x//60}:{x%60:02d}"


def where(cue):
    for k, v in {"HOOK": hook, **secs}.items():
        if cue.lower() in v.lower():
            return k


LOOPS = {
    "Loop1": ("that same study held a second result", "Two buds."),
    "Loop2": ("summary and its full text disagree", "the full text says they did not sprout"),
    "Cuoi": ("there's a fair way to test it yourself", "Here's the honest scoreboard"),
}
for n, (a, b) in LOOPS.items():
    print(n, where(a), f(at(a)), "->", where(b), f(at(b)))
print("nobody/no one:", len(re.findall(r"nobody|no one", body, flags=re.I)))
sents = [x for x in re.split(r"(?<=[.!?])\s+", body.strip()) if x]
c = sum(1 for x in sents if re.search(r"\b\w+'(s|t|re|ll|ve|d|m)\b", x))
print("contractions", round(100 * c / len(sents)), "%")
print("ACTION_TIP callback in KET:", "make three or four cuttings, not one" in secs["KẾT"].lower())
