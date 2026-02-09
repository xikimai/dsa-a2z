"""
Warmup 2: Matrix Chain Multiplication
=====================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum scalar multiplications for the matrix chain.

EXAMPLES
--------
  solve([10, 30, 5, 60]) -> 4500
  solve([40, 20, 30, 10, 30]) -> 26000
  solve([10, 20, 30]) -> 6000

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Interval DP. dp[i][j] = min cost to multiply matrices i..j. Iterate by interval length, try all split points k.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(dims: list[int]) -> int:
    """Return minimum scalar multiplications for the matrix chain."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    dims = [int(x) for x in tokens]
    print(solve(dims))
