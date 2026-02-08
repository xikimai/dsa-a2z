"""
Warmup 3: First Non-Repeating Character
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given a string of lowercase letters, find the first character that
appears exactly once. If no such character exists, return '_'.

INPUT FORMAT
------------
A single string of lowercase letters.

OUTPUT FORMAT
-------------
A single character — the first non-repeating character, or '_' if none.

CONSTRAINTS
-----------
- 0 <= len(s) <= 10^5
- s consists of lowercase English letters only

EXAMPLES
--------
Input:
  aabbcdd
Output: c

Input:
  aabb
Output: _

Input:
  a
Output: a

HINT
----
Build a frequency map first. Then scan the string again from left
to right and return the first character with count == 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> str:
    """Return first character appearing exactly once, or '_' if none."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
