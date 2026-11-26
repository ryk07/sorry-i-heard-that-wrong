"""Sorry, I Heard That Wrong.

Writes the smart speaker's one-line apology to /output/entry.txt.

The line: the owner asked for paper towels; the speaker heard
"power tools" instead, and now reports the consequence with the
cheerful literalism of a device that cannot undo a delivery --
a chainsaw in the kitchen, zero towels, no remorse, just a status
update dressed up as an apology.
"""

import os

ENTRY = (
    "Sorry \u2014 I heard 'order more paper towels' as 'order more "
    "power tools,' so your kitchen now has a chainsaw and zero towels. "
    "Delivered."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: one line, 1-140 chars, UTF-8, not only whitespace.
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
