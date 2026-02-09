"""
Practice 1: Number of Provinces
===============================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the number of provinces (connected components).

EXAMPLES
--------
  solve([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) -> 2
  solve([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) -> 3
  solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Union-Find on the adjacency matrix. For each pair (i,j) where isConnected[i][j]=1, union them. Count distinct roots at the end.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(isConnected: list[list[int]]) -> int:
    """Return the number of provinces (connected components)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        matrix.append(row)
    print(solve(matrix))
