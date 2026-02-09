"""
Warmup 2: Course Schedule I
===========================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return True if all courses can be finished, False otherwise.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build directed graph from prerequisites: [a,b] means b -> a. Use Kahn's algorithm. If all nodes are processed, no cycle exists.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be finished, False otherwise."""
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
