#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry writer (stdlib only).

Writes the two-part micro-confession (To: line + the unsent line itself)
to $OUTPUT_DIR/entry.txt (default /output), no trailing newline.
"""
import os

ENTRY = (
    "To: Grandma, who taught me to write letters\n"
    "I finally wrote you the letter you always asked for, "
    "and I finished it the week after your funeral."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
