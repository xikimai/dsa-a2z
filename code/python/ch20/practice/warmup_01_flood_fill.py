"""
Warmup 1: Flood Fill
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid of integers (image), a starting pixel (sr, sc),
and a new color, perform a flood fill: change the starting pixel and
all 4-directionally connected pixels of the same original color to
the new color.

EXAMPLES
--------
>>> solve([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
[[2,2,2],[2,2,0],[2,0,1]]

CONSTRAINTS
-----------
- 1 <= m, n <= 50
- 0 <= image[i][j], color < 2^16
- 0 <= sr < m, 0 <= sc < n
"""


def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """Flood fill starting from (sr, sc) with new color."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    sr, sc, color = int(first_line[2]), int(first_line[3]), int(first_line[4])
    image = []
    for _ in range(rows):
        image.append(list(map(int, input().split())))
    result = solve(image, sr, sc, color)
    for row in result:
        print(" ".join(map(str, row)))
