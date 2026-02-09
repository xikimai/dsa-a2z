"""
Practice 5: Count Numbers with Unique Digits
============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return count of numbers in [1, n] with all unique digits.

EXAMPLES
--------
  solve(20) -> 19
  solve(100) -> 90
  solve(10) -> 10

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Digit DP. Process digits of n from left to right. Track: - Position in the number

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int) -> int:
    """Return count of numbers in [1, n] with all unique digits."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.read().strip())
    print(solve(n))
