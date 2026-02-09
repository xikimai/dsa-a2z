"""
Practice 2: Burst Balloons
==========================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return maximum coins from bursting all balloons.

EXAMPLES
--------
  solve([3, 1, 5, 8]) -> 167
  solve([1, 5]) -> 10
  solve([7]) -> 7

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Interval DP. Add boundary 1s. dp[i][j] = max coins from bursting balloons in [i..j]. Think about which balloon is burst LAST.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return maximum coins from bursting all balloons."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    nums = [int(x) for x in tokens]
    print(solve(nums))
