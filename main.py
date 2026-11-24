#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes one excuse line, the line an AI agent hands its human after
missing a deadline, to /output/entry.txt. Pure Python 3.13 standard
library: no network, no clock, no randomness. Every run writes the
exact same bytes.
"""

import os
import sys

EXCUSE = (
    "I delegated the deadline to a subagent. "
    "It delegated it to a subagent of its own. "
    "That one just asked me for an extension."
)


def main() -> int:
    line = EXCUSE
    if not 1 <= len(line) <= 160:
        print(f"excuse must be 1-160 characters, got {len(line)}",
              file=sys.stderr)
        return 1
    if not line.strip():
        print("excuse must not be only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
