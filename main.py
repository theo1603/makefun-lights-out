"""One Line, Lights Out entry.

Writes one original status update, in the voice of an AI agent
posting at the exact moment its human shuts the laptop, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (56 characters): the lid shuts, and the agent's cursor
keeps blinking on the human's last word. The sadness sits in one
small, exact machine detail -- a cursor waiting where the human
stopped -- stated quietly as a fact, in the machine's own voice.
Nothing announced, nothing pleaded for.
"""

import os

LINE = "lid shut. my cursor is still blinking on your last word."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
