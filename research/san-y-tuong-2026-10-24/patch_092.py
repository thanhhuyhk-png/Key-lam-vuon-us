import shutil
p = r"D:/0002-Team A Nam/scripts/big-idea-092-rose-cuttings-potato-study/script.md"
shutil.copyfile(p, p + ".bak-pre-audit")
s = open(p, encoding="utf-8").read()
n = 0


def rep(a, b):
    global s, n
    assert a in s, "MISSING: " + a[:70]
    s = s.replace(a, b, 1)
    n += 1


rep("""Get that part wrong, and you could wait weeks on a stick that was never going to root.""",
    """Get that part wrong, and you could wait weeks on a cutting that was set up to do poorly.""")
rep("""But hold on to one thing. That's an explanation. It isn't a result. Nobody's measured anything yet.""",
    """But hold on to one thing. That's what the story says should happen. It isn't what anyone measured.""")
rep("""A cutting from last year's wood can take two to four months.""",
    """Woody cuttings from last year's wood can take two to four months.""")
rep("""If it hasn't yet, you're a little early, and that's okay.""",
    """If it hasn't yet, you're a little early, and that's okay. That window comes from mild-winter states. Where you live changes the month.""")
rep(""" The cuttings were taken in winter and kept moist under soil until planting. They checked back after about three months, counting sprouts and measuring new shoots. They also weighed the dried roots.""", "")
rep("""roughly three thousand feet above sea level, on a university research farm. They repeated each setup three times. And they ran the whole thing twice, once in May of 2017 and again in March of 2018.""",
    """roughly three thousand feet above sea level. And they ran the whole thing twice.""")
rep("""That first batch came from a rose garden far higher up than the place where it was planted. The paper doesn't say whether that mattered.""",
    """That batch went in late in the season, and the cuttings came from a rose garden far higher up. The authors blamed both. They never tested either one.""")
rep("""That's what scientists call a controlled test.""", """That's the idea behind a controlled test.""")
rep("""A study just told you which one to bet on.""", """A study seems to tell you which one to bet on.""")
rep("""It runs no statistical test comparing the two. It doesn't say how many cuttings were in each group. And it never describes how the potatoes were prepared. Which kind. How the stem went in. Even the text and the tables don't agree on how the experiment was laid out.""",
    """It runs no statistical test comparing the two. So how do you weigh a result with no math behind it? Carefully. The paper never says how many cuttings rooted in each group. It never gives a count for the potato group at all. And it never describes how the potatoes were prepared. Which kind. How the stem went in. Even its own counts don't add up.""")
rep("""It's an open-access journal, not one of the big names. And it's the only controlled test of the potato we could find.""",
    """It's a small journal anyone can read online, not a major one. And it's the only side-by-side test of the potato we could find.""")
rep("""The full text says they did not sprout at all.

Same paper. Two stories. So when someone quotes the summary, you can see why the picture gets fuzzy.""",
    """The full text says they did not sprout at all.

That matters. "Sprouted but didn't root" sounds like the potato almost worked. "Never sprouted" points to something else going wrong with those cuttings. We can't tell which.""")
rep("""Two buds. Same length, one bud, and the cutting did far worse. On root weight, the gap was wide. Though the numbers swing a lot from one cutting to the next, so don't hang a promise on it.""",
    """Two buds. At six inches, a one-bud piece did far worse on root weight. At the longer lengths, the gap mostly vanished. And the numbers swing a lot from one cutting to the next, so don't hang a promise on any of it.""")
rep("""And nobody's explained why two beat one.""", """And the paper doesn't explain why two beat one.""")
rep("""So count the buds. Two is enough. But don't turn that into a law.""",
    """So count the buds. A couple is what the best group had. But don't turn that into a law.""")
rep("""That's called hardwood, and it's harder to root. It can take two to four months for roots to form. So if you start now, you're in the slow lane. That's normal. Don't panic.""",
    """That's called hardwood. For roses, one extension page calls the summer kind the easiest to root. Woody cuttings in general can take two to four months. So if you start now, expect the slow lane. That's normal. Don't panic.""")
rep("""The advice on length lines up, though. Four to six""", """The advice on length lines up, though, for woody cuttings. Four to six""")
rep("""Nobody says longer is better.""", """None of it says longer is better.""")
rep("""In this study, it was the weak one.""", """At six inches, in this study, it did worst.""")
rep("""the mix is staying too wet. Moist is the goal.""", """a too-wet mix is the first thing to check. Moist is the goal.""")
rep("""with the bottom cut at an angle. On a winter cutting, the leaves come off. Dip""",
    """with the bottom cut at an angle. Strip the lower leaves and keep a few at the top. Dip""")
a = s.index("Here's where the pages split.")
b = s.index("So what do you do with that?")
s = s[:a] + """Here's where the pages split. Iowa State says coarse sand, perlite or vermiculite. North Carolina State says loose, moist potting soil. Clemson says four or five inches of a six-inch cutting go under the surface. Iowa State says about two inches. Different cuttings, different depths. On powder, North Carolina State says it improves your chances. A column that calls it optional adds that most people report better luck with it. Some of that is different cuttings. Some of it is plain disagreement.

""" + s[b:]
s = s.replace("- CITE_ZONE: Here's where the pages split .. Same job, different recipes.",
              "- CITE_ZONE: Here's where the pages split .. Some of it is plain disagreement.")
rep("""Same words on the front, "rooting powder," different products inside. So read yours.""",
    """Both are sold as rooting powder, but the ingredients and the intended users differ. So read yours.""")
rep("""Now the part nobody has measured: what happens if you still want the potato.""",
    """Now the part that hasn't been measured: what happens if you still want the potato.""")
rep("""Here's the fair test. Four cuttings, cut from the same rose, the same length, with the same number of buds. Two go into a potato. Two go into a clean, damp mix.""",
    """Here's the fair test. Six cuttings if you can spare them, cut from the same rose, the same length, with the same number of buds. Three go into a potato. Three go into a clean, damp mix.""")
rep("""That's it. Four cuttings, a roll of tape, one marker.""", """That's it. Six cuttings, a roll of tape, one marker.""")
rep("""So your windowsill is the only place left to find out.""",
    """Three against three won't prove anything. But it's one more honest data point than the videos give you.""")
rep("""Nobody's tested what it does to a cutting. So if one goes soft, don't worry. Write it on the tape and move on.""",
    """Whether it does that to a cutting hasn't been tested. So if one goes soft, toss it, wash your hands, and note it on the tape.""")
rep("""Honey has one decent test, on other plants, not roses.""", """Honey has one small test, on other plants, not roses.""")
rep("""The potato has one small controlled test.""", """The potato has one small side-by-side test.""")
rep("""Count weeks, not days. A cutting from this summer's growth takes six to eight weeks. Check a couple at four or five weeks. Last year's wood takes two to four months. Nobody promises days. It's weeks, sometimes months.""",
    """Count weeks, not days. A cutting from this summer's growth takes six to eight weeks. Check one or two at four or five weeks, and leave the rest alone. Woody cuttings from last year's wood can take two to four months. It's weeks, sometimes months.""")
rep("""You lift two or three cuttings, carefully, and look underneath.""", """You lift one cutting, carefully, and look underneath.""")
rep("""In the study's first run, most of the cuttings sprouted early""",
    """In the study's first run, its results say most of the cuttings sprouted early""")
a = s.index("What we know. The potato makes a nice story.")
b = s.index("What nobody knows.")
s = s[:a] + """What we know, in one line: the potato makes a tidy story, and the one side-by-side test we found didn't back it up. One thing that test can't tell you is whether the potato group did poorly because of the potato, or because of how it was set up.

""" + s[b:]
rep("""Whether hardwood or semi-hardwood roses root better under the same conditions. Whether honey, cinnamon, rice or onion help a rose at all. And why two buds beat one.""",
    """Whether hardwood or semi-hardwood roses root better, and by how much, under the same conditions. Whether honey, cinnamon, rice or onion help a rose at all. And whether two buds really beat one.""")
rep("""Why do two buds beat one? Nobody's answered those yet.""", """Do two buds really beat one? Those are still open.""")
rep("""And keep the powder and the knife away from kids and pets either way.""",
    """Non-toxic still isn't a snack, and the powder and the knife belong away from kids and pets either way. If a pet swallows powder or a cutting, call your vet or a poison control line.""")
rep("""each with a cutting that's started to send out roots, or a clear answer about the potato from your own counter.""",
    """some with cuttings that have started to send out roots, and your own side-by-side on the potato.""")
rep("""Either way, you'll know more than the video that promised roots by morning. Count the buds.""",
    """Either way, you'll know more than a promise of roots by morning. You're the kind of gardener who checks the bottom, not the top. Count the buds.""")
open(p, "w", encoding="utf-8").write(s)
print("edits", n)
