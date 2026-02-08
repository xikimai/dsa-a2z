"""
Solution for Challenge 1: Largest Rectangle in Histogram
============================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a monotonic stack (increasing). When a shorter bar arrives, pop and
compute area using the popped height and width from stack boundaries.
A sentinel of 0 at the end flushes remaining bars.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(heights: list[int]) -> int:
    """Return the area of the largest rectangle in the histogram."""
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        curr = heights[i] if i < n else 0  # sentinel
        while stack and heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    heights = list(map(int, input().strip().split()))
    print(solve(heights))
