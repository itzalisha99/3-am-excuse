"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

The wallet has watched its human long enough to know the pattern:
every 3 AM signature is a top-buy, so tonight it declines.
"""

import os

ENTRY = "I checked your transaction history. At 3 AM you only ever buy the top. Declined."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
