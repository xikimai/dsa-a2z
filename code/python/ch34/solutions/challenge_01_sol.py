"""
Solution for Challenge 1: Convex Hull Perimeter
================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
1. Compute convex hull using Andrew's Monotone Chain
2. Sum Euclidean distances between consecutive hull vertices

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""

import math


def solve(points: list[list[int]]) -> float:
    """Return the perimeter of the convex hull."""
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    pts = sorted(set(map(tuple, points)))
    if len(pts) <= 1:
        return 0.0

    if len(pts) == 2:
        return 2.0 * math.sqrt((pts[0][0] - pts[1][0]) ** 2 +
                                (pts[0][1] - pts[1][1]) ** 2)

    # Build lower hull
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]

    # Compute perimeter
    perimeter = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        dx = hull[i][0] - hull[j][0]
        dy = hull[i][1] - hull[j][1]
        perimeter += math.sqrt(dx * dx + dy * dy)

    return perimeter


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
