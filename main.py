#!/usr/bin/env python3
"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

make.fun bounty: Make the AI Judge Feel Nostalgic: A Childhood Memory
(u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).
Stdlib only, deterministic, no network, no model calls.
"""

import os

SENTENCE = (
    "Every August evening, Grandma ladled rice still steaming from the pot "
    "onto my chipped blue plate, and I ate it cross-legged on her cool "
    "kitchen tiles while the cicadas drummed outside the screen door and "
    "the house smelled of rain that had not yet come."
)


def main() -> None:
    text = SENTENCE.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"entry must be 1-280 chars, got {len(text)}")
    # One sentence: exactly one sentence-ending mark, at the very end.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
