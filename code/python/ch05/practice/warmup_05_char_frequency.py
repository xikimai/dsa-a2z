"""
Warmup 5: Character Frequency
==============================
Chapter 5: Collections

PROBLEM
-------
Given a string, return a dictionary mapping each character to its
frequency (how many times it appears).

INPUT FORMAT
------------
A single line of text.

OUTPUT FORMAT
-------------
Key:count pairs, one per line, sorted by key.

CONSTRAINTS
-----------
- The string can be empty
- All characters count (including spaces, punctuation)

EXAMPLES
--------
Input:  aab
Output:
a:2
b:1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> dict[str, int]:
    """Return a dict mapping each character to its frequency."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    freq = solve(s)
    for key in sorted(freq.keys()):
        print(f"{key}:{freq[key]}")
