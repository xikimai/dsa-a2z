"""
Practice 3: Pacific Atlantic Water Flow
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid of heights, water flows from a cell to any
4-directionally adjacent cell with equal or lower height. The Pacific
ocean touches the top and left edges; the Atlantic touches the bottom
and right edges. Return all cells from which water can reach BOTH oceans.

EXAMPLES
--------
>>> solve([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

CONSTRAINTS
-----------
- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5
"""


def solve(heights: list[list[int]]) -> list[list[int]]:
    """Return sorted list of cells that can reach both oceans."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    heights = []
    for _ in range(rows):
        heights.append(list(map(int, input().split())))
    result = solve(heights)
    for cell in result:
        print(cell[0], cell[1])
