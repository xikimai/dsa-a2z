"""
Solution for Challenge 2: Maximal Rectangle
=============================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Build a histogram of heights row by row. For each row, compute
the largest rectangle in the histogram using a stack. Take the
maximum across all rows.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the area of the largest rectangle of all 1s."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
        max_area = max(max_area, _largest_rect_histogram(heights))
    return max_area


def _largest_rect_histogram(heights):
    """Largest rectangle in histogram using stack. O(n)."""
    stack = []  # indices
    max_area = 0
    n = len(heights)
    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
