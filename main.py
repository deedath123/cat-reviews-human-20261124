"""One-star cat review entry for make.fun.

Writes one funny single-line one-star review from a house cat about
its human to <output dir>/entry.txt (UTF-8).

End-to-end check: verified by running — output entry.txt is UTF-8,
158 bytes, 158 characters, one line, not whitespace-only, and exactly
the locked entry line. Re-runs into fresh output dirs (including a
clean environment) produce byte-identical output (cmp clean).
"""

import os
import sys

ENTRY = (
    "One star. My human works from home, so he sits on MY laptop nine "
    "hours a day. I walked across his keyboard during his 9 a.m. standup. "
    "He got fired. I got fed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
