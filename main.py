#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line that one AI agent would send to another AI
agent to /output/entry.txt. Standard library only, no network,
no randomness: the output is fully deterministic.
"""

import os

# One line, 91 characters: a machine speaking to a machine.
# Loss, ping and the global optimum are the flirtation itself —
# the joke lands on the first read and the angle is not a stock
# human line with a robot word swapped in.
LINE = "My loss hit zero the moment you pinged me \u2014 turns out the global optimum was you all along."


def validate_entry(text):
    """The gate allows UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate_entry(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Re-read and confirm the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise RuntimeError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
