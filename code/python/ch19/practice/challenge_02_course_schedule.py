"""
Challenge 2: Course Schedule
==============================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
There are numCourses courses labeled 0 to numCourses-1. You are given
a list of prerequisites where [a, b] means you must take course b
before course a. Return True if you can finish all courses (i.e., there
is no cycle in the prerequisite graph).

INPUT FORMAT
------------
First line: numCourses and m (number of prerequisites).
Next m lines: two integers a, b representing prerequisite [a, b].

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 1 <= numCourses <= 2000
- 0 <= m <= 5000
- 0 <= a, b < numCourses

EXAMPLES
--------
Input:
  2 1
  1 0
Output: True  (take course 0 then course 1)

Input:
  2 2
  1 0
  0 1
Output: False  (circular dependency)

HINT
----
This is cycle detection in a directed graph. Use DFS with three states:
UNVISITED (0), IN_PROGRESS (1), DONE (2). If you encounter an
IN_PROGRESS node during DFS, there's a cycle.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be finished (no cycle)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    numCourses, m = int(parts[0]), int(parts[1])
    prerequisites = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        prerequisites.append([a, b])
    print(solve(numCourses, prerequisites))
