"""
Practice 4: Row with Maximum 1s
=================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given a binary matrix where each row is sorted (all 0s come before all 1s),
find the row with the maximum number of 1s. Return the row index (0-indexed),
or -1 if there are no 1s. If multiple rows tie, return the first one.

INPUT FORMAT
------------
First line: two integers rows and cols.
Next rows lines: cols space-separated integers (0 or 1).

OUTPUT FORMAT
-------------
A single integer — the row index, or -1.

CONSTRAINTS
-----------
- 1 <= rows, cols <= 500
- matrix[i][j] is 0 or 1
- Each row is sorted (0s before 1s)

EXAMPLES
--------
Input:
  5 5
  0 0 0 1 1
  0 0 1 1 1
  0 0 0 0 1
  0 1 1 1 1
  0 0 0 0 0
Output: 3

Input:
  2 3
  0 0 0
  0 0 0
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(matrix: list[list[int]]) -> int:
    """Return index of the row with the maximum number of 1s, or -1."""
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
    print(solve(matrix))
