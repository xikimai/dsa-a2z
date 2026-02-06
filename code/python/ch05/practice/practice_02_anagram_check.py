"""
Practice 2: Anagram Check
==============================
Chapter 5: Collections

PROBLEM
-------
Given two strings, determine if they are anagrams of each other.
Two strings are anagrams if they contain the same characters with
the same frequencies, ignoring case.

INPUT FORMAT
------------
Two lines, each containing a string.

OUTPUT FORMAT
-------------
"True" or "False"

CONSTRAINTS
-----------
- Strings can be empty
- Comparison is case-insensitive
- Only alphabetic characters matter (but for simplicity, consider all chars)

EXAMPLES
--------
Input:
listen
silent
Output: True

Input:
hello
world
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s1: str, s2: str) -> bool:
    """Return True if s1 and s2 are anagrams (case-insensitive)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
