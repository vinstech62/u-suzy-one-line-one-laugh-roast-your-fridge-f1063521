#!/usr/bin/env python3
"""Roast Your Fridge — one-line roast writer.

Writes a single roast line about the author's own fridge to
/output/entry.txt (1-200 UTF-8 characters, exactly one line).
"""

import os

ENTRY = "My fridge's fingerprint-covered door is the only family portrait we have, and everyone in it is a smudge."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
