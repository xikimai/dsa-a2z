"""
Practice 5: Sort Characters by Frequency
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given a string, sort it by character frequency in descending order.
Characters with the same frequency should be sorted alphabetically
(ascending).

INPUT FORMAT
------------
A single string.

OUTPUT FORMAT
-------------
A string with characters sorted by frequency descending, with
alphabetical ascending tiebreak.

CONSTRAINTS
-----------
- 0 <= len(s) <= 10^5
- s consists of lowercase and/or uppercase English letters and digits

EXAMPLES
--------
Input:
  tree
Output: eert

Input:
  cccaaa
Output: aaaccc

Input:
  hello
Output: lleho

HINT
----
Build a frequency map. Sort unique characters by (-frequency, character)
to get descending frequency with alphabetical tiebreak. Then build the
result by repeating each character by its frequency.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> str:
    """Sort string characters by frequency descending, alpha ascending tiebreak."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
