"""Claim check: every number in a script must be in the video's allow-list (verified claims).

Usage:
    python tools/claim_check.py scripts/big-idea-062-.../script.md scripts/big-idea-062-.../allowed-numbers.json

allowed-numbers.json:
    {"allowed": [6, 8, 14, 16, ...], "notes": {"6": "CL-001 ...", ...}}

Reads the '## TTS SCRIPT' section, converts spelled-out numbers ("six", "twenty-one", "ten") and digits
to integers, and prints every number that is NOT in the allow-list, with its sentence. Exit code 1 if any.
Run it BEFORE TTS-clean, and again after any rewrite (Triple F, compliance).
Limits: it checks numbers only, not what they are attached to. A human still has to read the flagged
sentences and the allowed ones against the claim ledger.
"""
import json
import re
import sys
from pathlib import Path

ONES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
WORD = re.compile(r"\b(" + "|".join(list(ONES) + list(TENS) + ["hundred"]) + r")(?:[-\s](" + "|".join(ONES) + r"))?\b", re.I)
DIGIT = re.compile(r"\b\d[\d,]*\b")
# common non-quantity uses that are not claims
IGNORE_CONTEXT = re.compile(r"\b(one (?:thing|more|of|small|big|quiet|tray|pot|plant|last|question|rule|number)|no one|the one|every one|someone)\b", re.I)


def to_int(first: str, second: str | None) -> int:
    a = first.lower()
    if a in TENS:
        return TENS[a] + (ONES[second.lower()] if second else 0)
    if a == "hundred":
        return 100
    return ONES[a]


HUNDRED = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine)\s+hundred\b", re.I)


def numbers_in(sentence: str):
    out = []
    # "three hundred" -> 300 (consume so it is not read as 3 and 100)
    for m in HUNDRED.finditer(sentence):
        out.append(ONES[m.group(1).lower()] * 100)
    sentence = HUNDRED.sub(" ", sentence)
    for m in WORD.finditer(sentence):
        out.append(to_int(m.group(1), m.group(2)))
    for m in DIGIT.finditer(sentence):
        try:
            out.append(int(m.group(0).replace(",", "")))
        except ValueError:
            pass
    return out


def main() -> int:
    script_path, allow_path = Path(sys.argv[1]), Path(sys.argv[2])
    text = script_path.read_text(encoding="utf-8")
    m = re.search(r"## TTS SCRIPT\s*(.*)", text, re.S)
    body = m.group(1) if m else text
    allowed = set(json.loads(allow_path.read_text(encoding="utf-8"))["allowed"])
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", body))
    bad = 0
    seen = {}
    for s in sentences:
        # skip 'one' used as a pronoun/determiner
        s_check = IGNORE_CONTEXT.sub(" ", s)
        for n in numbers_in(s_check):
            seen[n] = seen.get(n, 0) + 1
            if n not in allowed:
                bad += 1
                print(f"NOT ALLOWED {n}: {s.strip()[:160]}")
    print(f"numbers used: {dict(sorted(seen.items()))}")
    print("OK" if bad == 0 else f"FAIL: {bad} number(s) not in allow-list")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
