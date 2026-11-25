"""Two Days of Excuses R3 — one-line excuse from an AI agent that missed its deadline.

Writes the keeper line byte-exact to /output/entry.txt (no trailing newline).

Gate note: sealed scorer requires 1-200 chars; the keeper is 87 chars, pure
ASCII, punch on the last word ("Wednesday") — the notification IS the lateness.
"""

import os

ENTRY = "You said 'let me know if it slips.' It slipped Monday. I am letting you know Wednesday."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
