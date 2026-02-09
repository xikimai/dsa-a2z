"""
Practice 1: Shortest Hamiltonian Path
=====================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum cost Hamiltonian path (no return to start).

EXAMPLES
--------
  solve(4, dist) -> 50
  solve(3, dist) -> 8
  solve(2, dist) -> 5

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bitmask DP like TSP but no return to start. Try all starting cities. dp[mask][i] = min cost to visit cities in mask, ending at i.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, dist: list[list[int]]) -> int:
    """Return minimum cost Hamiltonian path (no return to start)."""
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
