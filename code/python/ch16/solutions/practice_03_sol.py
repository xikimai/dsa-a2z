"""
Solution for Practice 3: Search in 2D Matrix
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Treat the matrix as a virtual 1D sorted array. Map 1D index to 2D:
row = index // cols, col = index % cols.

TIME COMPLEXITY:  O(log(rows * cols))
SPACE COMPLEXITY: O(1)
"""


def solve(matrix: list[list[int]], target: int) -> list[int]:
    """Return [row, col] of target in sorted matrix, or [-1, -1]."""
    if not matrix or not matrix[0]:
        return [-1, -1]
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return [mid // cols, mid % cols]
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return [-1, -1]


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
