"""Everyday Things, Two Lines, Longer Run.

Writes exactly two lines to /output/entry.txt.
Line 1: one everyday thing (a toaster) explained to a 10-year-old in a
single vivid sentence built on one analogy.
Line 2: one sentence on why the analogy works -- what it maps and
what it leaves out.
Deterministic, offline, stdlib only.
"""

import os

ENTRY = (
    "A toaster is a tiny tanning booth where bread stands to get brown on both sides until it pops up golden.\n"
    "It maps heat browning both sides like a tan, but leaves out that glowing wires, not sunlight, do the browning, and the timer decides when it pops up.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
