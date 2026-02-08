"""
Solution for Practice 4: Row with Maximum 1s
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
For each row, binary search for the first 1. The row where the first 1
appears earliest (smallest index) has the most 1s.

TIME COMPLEXITY:  O(rows * log(cols))
SPACE COMPLEXITY: O(1)
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
