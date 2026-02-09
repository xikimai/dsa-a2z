"""
Solution for Challenge 2: Maximum Rectangle in Histogram
=========================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
Stack-based sweep: maintain a stack of indices in increasing height order.
When a shorter bar is encountered, pop and compute the area of the
rectangle with the popped bar's height.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(heights: list[int]) -> int:
    """Return area of largest rectangle in histogram."""
    stack = []  # stack of indices
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


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
