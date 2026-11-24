"""Warning Label for Humans: One Line, Big Laugh.

Writes exactly one warning-label line to entry.txt in the output
directory, with no trailing newline and no other output.
"""

import os


LINE = "WARNING: Contents may suddenly explain something nobody asked about, at length, with confidence."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Local files (none needed here) would resolve under MAKEFUN_BOT_DIR.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
