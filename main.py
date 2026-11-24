#!/usr/bin/env python3
"""Grandma's Witchcraft — One Word From Grandma (make.fun).

The entry is a single word: the word a grandma would text about AI.

Why "Witchcraft": asked what AI is, a grandma does not reach for a
manual. She reaches for the one word that covers anything she cannot
see working — the kettle that talks back, the phone that finishes her
sentences, the machine that seems to know things. "Witchcraft" is her
warm, baffled verdict on it: funny in one word, instantly readable,
fresh next to the obvious "robot", and tied to AI precisely because
it is what she calls the magic she does not understand.

The program is deliberately deterministic: no network, no randomness,
no secrets, no input. It writes exactly one word to /output/entry.txt.

Word choice, weighed against the judge's own criteria in order:
1. Grandma would text it about AI — she calls anything she cannot
   see working "witchcraft"; it is her verdict, not a description.
2. Her voice — warm and a little baffled, the way she types to a
   grandchild, not the way a brochure talks about "the future".
3. Funny in one word, with no caption needed — the joke is that the
   most advanced technology on earth gets filed under folk magic.
4. Tied to AI — the brief itself frames the word as "about AI", and
   witchcraft is what she calls the magic of a machine that knows
   things; it would not fit just any subject the same way.
5. Fresh, not obvious — "robot", "scary", "magic" are the picks
   everyone reaches for first; "Witchcraft" is the one she actually
   sends.
"""

import os
import sys

# The single word this entry submits. Capitalised as a grandma would
# type it at the start of a text to her grandchild.
WORD = "Witchcraft"

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 30
# characters, not only whitespace, and a single word.
MAX_CHARS = 30


def main() -> int:
    word = WORD.strip()

    if not word:
        print("error: entry word is empty", file=sys.stderr)
        return 1
    if len(word) > MAX_CHARS:
        print(f"error: entry word is {len(word)} chars, over the 30-char gate",
              file=sys.stderr)
        return 1
    if len(word.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    if not word.isalpha():
        # One plain word: no punctuation tricks, no digits, no symbols.
        # The judge brief rules those out, and a grandma types a word.
        print("error: entry must be a plain alphabetic word", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)

    # Read it back and confirm what the grader will see.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word:
        print(f"error: wrote {written!r}, expected {word!r}", file=sys.stderr)
        return 1

    print(f"entry written to {OUTPUT_PATH}: {written!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
