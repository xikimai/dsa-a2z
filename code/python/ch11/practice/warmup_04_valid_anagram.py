"""
Warmup 4: Valid Anagram
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given two strings, determine if they are anagrams of each other.
Two strings are anagrams if they contain the same characters with
the same frequencies.

INPUT FORMAT
------------
Two lines, each containing a string of lowercase letters.

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 0 <= len(s1), len(s2) <= 10^5
- Strings consist of lowercase English letters only

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

Input:
  ab
  ba
Output: True

HINT
----
Build a frequency map for one string, then decrement counts using
the other string. If all counts end up zero, they're anagrams.
(Quick shortcut: if lengths differ, return False immediately.)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    print(solve(s1, s2))
