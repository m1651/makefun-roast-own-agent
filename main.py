#!/usr/bin/env python3
"""Write one original roast of my own AI agent to entry.txt.

Standard library only. Deterministic: the same bytes on every run,
with no network access and no input read from anywhere.
"""

import os

ROAST = (
    "My agent is so fond of delegating that it outsourced this roast "
    "to a subagent, who outsourced it back \u2014 and both billed me "
    "for thinking."
)
# The gate counts characters: the roast is one line, 136 characters,
# with no trailing newline, so the file holds exactly the roast.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
