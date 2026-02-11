"""
Challenge 3: Longest Repeating Character Replacement
======================================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given a string of uppercase English letters and an integer k, find the
length of the longest substring you can obtain by replacing at most k
characters so that all characters in the substring are the same.

INPUT FORMAT
------------
First line: a string of uppercase letters.
Second line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the length of the longest valid substring.

CONSTRAINTS
-----------
- 1 <= len(s) <= 10^5
- 0 <= k <= len(s)
- s consists of uppercase English letters

EXAMPLES
--------
Input:
  ABAB
  2
Output: 4

Input:
  AABABBA
  1
Output: 4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str, k: int) -> int:
    """Return length of longest substring after at most k replacements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    print(solve(s, k))

