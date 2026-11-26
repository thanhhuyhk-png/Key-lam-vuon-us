p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/seo-en.md"
s = open(p, encoding="utf-8").read()
n = 0


def rep(a, b):
    global s, n
    assert a in s, "MISSING: " + a[:60]
    s = s.replace(a, b, 1)
    n += 1


rep("But that same study held a second result—about the cutting itself—that matters more than the potato debate.",
    "That same study held a second result, about the cutting itself. This video goes through what it found, what it can't tell you, and a fair way to test the potato yourself.")
rep("Why the potato trick sounds scientifically sound (and why a good explanation isn't proof)",
    "Why the potato trick sounds convincing (and why an explanation isn't a result)")
rep("What one controlled study found when it compared rose cuttings in potatoes vs. soil",
    "What one small side-by-side study found when it compared rose cuttings in potatoes vs. soil")
rep("Why the result you've heard about might be misleading (the paper's summary and full text don't agree on one detail)",
    "One detail where the paper's own summary and full text disagree")
rep("Viral videos and garden blogs repeat it.", "Viral videos repeat it.")
rep("We found gaps between what viral claims promise and what the evidence shows.",
    "The evidence we could read is thin, and we say so.")
rep("explains why most of the interesting finding has nothing to do with potatoes,",
    "explains the second result about the cutting itself,")
rep("## 📚 REFERENCES", "## 📚 REFERENCES (sources checked 10/24/2026)")
rep('- Wali, Shafiqi & Ahmadi (2019). "Rose Propagation Using Potato as a Growth Medium." *International Journal of Innovative Research and Scientific Studies*, 2(4):55–61.',
    '- Wali, Shafiqi & Ahmadi (2019). "Effect of cutting size, number of buds and potatoes on sprouting and adventitious root formation of rose semi hardwood cuttings." *International Journal of Innovative Research and Scientific Studies*, 2(4):55–61.')
rep('Clemson HGIC, C. Tanner. "Hardwood', 'Clemson HGIC. "Hardwood')
rep("**Kiểu: A — Câu hỏi kích bình luận**\n\n", "")
open(p, "w", encoding="utf-8").write(s)
print("edits", n)
