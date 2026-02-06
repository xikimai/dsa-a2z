"""
Practice 03: Distance Between Two Points
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given the coordinates of two points in a 2D plane, compute the Euclidean
distance between them.

Formula:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

INPUT FORMAT
------------
A single line containing four space-separated floats: x1 y1 x2 y2.

OUTPUT FORMAT
-------------
Print a single float — the distance between the two points.

CONSTRAINTS
-----------
-10^4 <= x1, y1, x2, y2 <= 10^4

EXAMPLES
--------
Input:  0 0 3 4
Output: 5.0

Input:  0 0 0 0
Output: 0.0

Input:  1 1 4 5
Output: 5.0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the Euclidean distance between points (x1, y1) and (x2, y2)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    x1, y1, x2, y2 = map(float, input().split())
    print(solve(x1, y1, x2, y2))
