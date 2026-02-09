"""
Warmup 1: Traveling Salesman Problem (TSP)
==========================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum cost to visit all cities and return to start.

EXAMPLES
--------
  solve(4, dist) -> 80
  solve(3, dist) -> 23
  solve(2, dist) -> 10

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bitmask DP. State dp[mask][i] = min cost to visit exactly the cities in mask, ending at city i. Iterate over all masks and transitions.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, dist: list[list[int]]) -> int:
    """Return minimum cost to visit all cities and return to start."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    dist = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        dist.append(row)
    print(solve(n, dist))
