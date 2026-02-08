"""
Challenge 1: Walls and Gates
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid where -1 = wall, 0 = gate, 2147483647 = empty room,
fill each empty room with the distance to its nearest gate. If a room
cannot reach any gate, leave it as 2147483647.

EXAMPLES
--------
>>> INF = 2147483647
>>> solve([[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]])
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

CONSTRAINTS
-----------
- 1 <= m, n <= 250
- grid[i][j] is -1, 0, or 2147483647
"""

INF = 2147483647


def solve(rooms: list[list[int]]) -> list[list[int]]:
    """Fill each empty room with distance to nearest gate."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    rooms = []
    for _ in range(rows):
        rooms.append(list(map(int, input().split())))
    solve(rooms)
    for row in rooms:
        print(" ".join(map(str, row)))
