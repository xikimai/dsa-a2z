"""
Challenge 3: Number of Islands II
=================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return island count after each land addition.

EXAMPLES
--------
  solve(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]) -> [1, 1, 2, 3]
  solve(1, 1, [[0, 0]]) -> [1]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Online Union-Find: for each new land position, create a new component, then try to union with 4-directional neighbors that are already land.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(m: int, n: int, positions: list[list[int]]) -> list[int]:
    """Return island count after each land addition."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    m = int(tokens[idx]); idx += 1
    n = int(tokens[idx]); idx += 1
    p = int(tokens[idx]); idx += 1
    positions = []
    for _ in range(p):
        r = int(tokens[idx]); idx += 1
        c = int(tokens[idx]); idx += 1
        positions.append([r, c])
    result = solve(m, n, positions)
    print(" ".join(map(str, result)))
