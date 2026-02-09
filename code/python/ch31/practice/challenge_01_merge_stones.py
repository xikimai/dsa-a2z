"""
Challenge 1: Minimum Cost to Merge Stones
=========================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum cost to merge all stones, or -1 if impossible.

EXAMPLES
--------
  solve([3, 2, 4, 1], 2) -> 20
  solve([3, 5, 1, 2, 6], 3) -> 25
  solve([3, 2, 4, 1], 3) -> -1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Interval DP. Each merge reduces pile count by k-1. So we need (n-1) % (k-1) == 0 for it to be possible. dp[i][j] = min cost

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(stones: list[int], k: int) -> int:
    """Return minimum cost to merge all stones, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    k_val = int(tokens[idx]); idx += 1
    stones = []
    for _ in range(n):
        stones.append(int(tokens[idx])); idx += 1
    print(solve(stones, k_val))
