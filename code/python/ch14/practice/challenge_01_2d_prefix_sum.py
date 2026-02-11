"""
Challenge 1: 2D Prefix Sum and Range Query
============================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given a 2D matrix and multiple queries, each specifying a rectangle
[r1, c1, r2, c2], return the sum of all elements in that rectangle
for each query. Use 2D prefix sums for efficient querying.

INPUT FORMAT
------------
First line: two integers rows and cols.
Next rows lines: cols space-separated integers.
Next line: integer q (number of queries).
Next q lines: four integers r1, c1, r2, c2.

OUTPUT FORMAT
-------------
A list of rectangle sums.

CONSTRAINTS
-----------
- 1 <= rows, cols <= 500
- -10^6 <= matrix[i][j] <= 10^6
- 1 <= q <= 10^5
- 0 <= r1 <= r2 < rows, 0 <= c1 <= c2 < cols

EXAMPLES
--------
Input:
  3 3
  1 2 3
  4 5 6
  7 8 9
  2
  0 0 2 2
  1 1 2 2
Output: [45, 28]

Input:
  1 1
  5
  1
  0 0 0 0
Output: [5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(matrix: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return list of rectangle sums for each query."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    print(solve(matrix, queries))

