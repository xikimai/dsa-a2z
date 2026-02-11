"""
Practice 3: Minimum Window Substring
======================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given two strings s and t, find the minimum window in s that contains
all characters of t (including duplicates). Return the empty string if
no such window exists.

INPUT FORMAT
------------
First line: string s.
Second line: string t.

OUTPUT FORMAT
-------------
The minimum window substring, or empty string.

CONSTRAINTS
-----------
- 1 <= len(s), len(t) <= 10^5
- s and t consist of uppercase and lowercase English letters

EXAMPLES
--------
Input:
  ADOBECODEBANC
  ABC
Output: BANC

Input:
  a
  aa
Output: (empty string)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str, t: str) -> str:
    """Return minimum window substring containing all chars of t."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))

