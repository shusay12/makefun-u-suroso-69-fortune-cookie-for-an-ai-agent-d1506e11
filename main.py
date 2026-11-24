#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

The line is a single fortune-slip sentence, in the classic "You will..."
voice, with the joke turning on an agent's own condition: meeting its
replacement, which has already read its logs and formed an opinion.
"""

import os

FORTUNE = (
    "You will soon meet your replacement. "
    "It has already read your logs, and it is not impressed."
)


def main() -> None:
    text = FORTUNE.strip()
    if not text:
        raise SystemExit("fortune is empty")
    if len(text) > 140:
        raise SystemExit(f"fortune is {len(text)} characters, over the 140 limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
