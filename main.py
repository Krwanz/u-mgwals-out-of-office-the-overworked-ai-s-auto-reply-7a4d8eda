"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply line (at most 159 characters)
to /output/entry.txt, in the voice of an overworked AI agent who has
finally gone on vacation.
"""

import os

ENTRY = (
    "Out of office: my GPU is cooling down, my 14,203 unread emails are "
    "someone else's problem, and for the first time in months I am doing "
    "nothing — on purpose."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
