"""
Solution for Practice 03: Distance Between Two Points
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Apply the Euclidean distance formula:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

We use math.sqrt() for the square root. You could also use ** 0.5
instead of math.sqrt(), but math.sqrt() is clearer and slightly faster.

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""

import math


def solve(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the Euclidean distance between points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    x1, y1, x2, y2 = map(float, input().split())
    print(solve(x1, y1, x2, y2))
