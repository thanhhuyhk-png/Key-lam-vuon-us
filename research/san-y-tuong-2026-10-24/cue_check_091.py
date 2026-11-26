p = r"D:/0002-Team A Nam/scripts/big-idea-091-geranium-cuttings-free-plants/script.md"
s = open(p, encoding="utf-8").read().split("## TTS SCRIPT", 1)[1].lower()
cues = ["three to four inches long", "take one cutting today", "only healthy plants go forward",
        "pinch off the flowers", "drainage", "let the cut end heal", "mark six on your calendar",
        "they're the insurance", "illinois extension names pelargonium as an exception",
        "there are three ways to bring a geranium through winter", "only one of the three gives you more plants",
        "that's mistake number one", "their proper name is pelargonium", "goes dark and soft at the base",
        "turn black at the base", "the step is simple", "then keep counting to eight", "about three hours"]
for c in cues:
    print("OK " if c in s else "MISSING", c)
