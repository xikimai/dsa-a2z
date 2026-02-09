"""
Practice 2: Parallel Courses
============================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return minimum semesters to complete all courses, or -1 if impossible.

EXAMPLES
--------
  solve(3, [[1, 3], [2, 3]]) -> 2
  solve(3, [[1, 2], [2, 3], [3, 1]]) -> -1
  solve(4, [[1, 2], [1, 3], [2, 4], [3, 4]]) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Level-based Kahn's BFS (1-indexed nodes). Count BFS levels = minimum semesters.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(n: int, relations: list[list[int]]) -> int:
    """Return minimum semesters to complete all courses, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    relations = []
    for _ in range(m):
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        relations.append([a, b])
    print(solve(n, relations))
