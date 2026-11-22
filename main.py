#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet moment for the
reader who has spent the day reading everyone else's words.
Deterministic: the same text on every run, no network, no randomness.
"""

import os
import stat

TEXT = (
    "You have read a hundred voices today. Set them down. "
    "Somewhere just past this page, rain is starting on a tin roof "
    "\u2014 not asking to be counted, not keeping score, just arriving, "
    "one drop at a time. Let the evening settle over you like that. "
    "Nothing here needs anything from you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
