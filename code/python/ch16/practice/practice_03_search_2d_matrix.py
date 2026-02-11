"""
Practice 3: Search in 2D Matrix
=================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given a 2D matrix where each row is sorted left to right and the first
element of each row is greater than the last element of the previous row,
search for a target value. Return [row, col] if found, [-1, -1] otherwise.

INPUT FORMAT
------------
First line: two integers rows and cols.
Next rows lines: cols space-separated integers.
Last line: a single integer (the target).

OUTPUT FORMAT
-------------
A list [row, col] or [-1, -1].

CONSTRAINTS
-----------
- 0 <= rows, cols <= 100
- -10^6 <= matrix[i][j] <= 10^6
- Matrix is fully sorted (row-major order)

EXAMPLES
--------
Input:
  3 4
  1 3 5 7
  10 11 16 20
  23 30 34 60
  3
Output: [0, 1]

Input:
  3 4
  1 3 5 7
  10 11 16 20
  23 30 34 60
  13
Output: [-1, -1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(matrix: list[list[int]], target: int) -> list[int]:
    """Return [row, col] of target in sorted matrix, or [-1, -1]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import sys
    lines = sys.stdin.read().split("\n")
    idx = 0
    rows, cols = map(int, lines[idx].split())
    idx += 1
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, lines[idx].split())))
        idx += 1
    target = int(lines[idx].strip())
    print(solve(matrix, target))
