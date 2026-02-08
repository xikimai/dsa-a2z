"""
Practice 3: Decode Ways
========================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
A message containing letters A-Z is encoded as numbers: 'A'->1, 'B'->2, ..., 'Z'->26.
Given a string of digits, return the number of ways to decode it.

EXAMPLES
--------
  s="12" -> 2  ("AB" or "L")
  s="226" -> 3  ("BZ", "VF", "BBF")
  s="06" -> 0  (leading zero is invalid)

CONSTRAINTS
-----------
- 1 <= len(s) <= 100
- s contains only digits

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> int:
    """Return the number of ways to decode the digit string."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
