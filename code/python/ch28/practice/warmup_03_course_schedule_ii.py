"""
Warmup 3: Course Schedule II
============================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return a valid course ordering, or [] if impossible.

EXAMPLES
--------
  solve(2, [[1, 0], [0, 1]]) -> []
  solve(1, []) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Kahn's algorithm on prerequisite graph. [a,b] means b -> a. Return result list if all nodes processed, else [].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return a valid course ordering, or [] if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    prereqs = []
    for _ in range(m):
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        prereqs.append([a, b])
    print(solve(n, prereqs))
