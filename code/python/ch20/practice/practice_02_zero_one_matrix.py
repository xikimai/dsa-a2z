"""
Practice 2: 01 Matrix
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n binary matrix mat, return the distance of the nearest 0
for each cell. The distance between two adjacent cells is 1.

EXAMPLES
--------
>>> solve([[0,0,0],[0,1,0],[1,1,1]])
[[0,0,0],[0,1,0],[1,2,1]]

CONSTRAINTS
-----------
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is 0 or 1
- There is at least one 0
"""


def solve(mat: list[list[int]]) -> list[list[int]]:
    """Return distance of each cell to nearest 0."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    mat = []
    for _ in range(rows):
        mat.append(list(map(int, input().split())))
    result = solve(mat)
    for row in result:
        print(" ".join(map(str, row)))
