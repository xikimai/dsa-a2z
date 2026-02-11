"""
Practice 3: Rat in a Maze
===========================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given an n x n maze where 1 = open and 0 = blocked, find all paths
from (0,0) to (n-1,n-1). The rat can move in four directions: Down (D),
Left (L), Right (R), Up (U). Return all valid paths sorted.

INPUT FORMAT
------------
First line: integer n (size of the maze).
Next n lines: n space-separated integers (0 or 1).

OUTPUT FORMAT
-------------
Each path as a string of direction characters, one per line, sorted.

CONSTRAINTS
-----------
- 1 <= n <= 8
- maze[i][j] is 0 or 1
- maze[0][0] and maze[n-1][n-1] are 1

EXAMPLES
--------
Input:
  4
  1 0 0 0
  1 1 0 1
  1 1 0 0
  0 1 1 1
Output:
  DDRDRR
  DRDDRR

Input:
  1
  1
Output:
  (empty string)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(maze: list[list[int]]) -> list[str]:
    """Return all paths from (0,0) to (N-1,N-1), sorted."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    result = solve(maze)
    for path in result:
        print(path)

