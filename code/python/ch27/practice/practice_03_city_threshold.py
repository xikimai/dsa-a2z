"""
Practice 3: Find City with Smallest Neighbors at Threshold
==========================================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return the city with smallest neighbors at threshold distance.

EXAMPLES
--------
  solve(4, edges, 4) -> 3
  solve(5, edges, 2) -> 0
  solve(2, [[0,1,5]], 5) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Floyd-Warshall for all-pairs shortest paths (bidirectional edges). Then for each city, count how many other cities are within threshold.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]], threshold: int) -> int:
    """Return the city with smallest neighbors at threshold distance."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        edges.append([u, v, w])
    threshold = int(data[idx]); idx += 1
    print(solve(n, edges, threshold))
