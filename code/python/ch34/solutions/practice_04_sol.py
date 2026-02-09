"""
Solution for Practice 4: Maximum Points on a Line
===================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
For each point i, compute the slope to every other point j.
Use GCD-normalized (dx, dy) as slope key to avoid floating point.
The maximum count for any slope + 1 (for point i itself) is the answer
for that anchor. Take the global maximum.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n)
"""

from math import gcd


def solve(points: list[list[int]]) -> int:
    """Return maximum number of collinear points."""
    n = len(points)
    if n <= 2:
        return n

    best = 1
    for i in range(n):
        slopes = {}
        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            # Normalize the slope direction
            if dx == 0:
                dy = 1  # vertical line
            elif dy == 0:
                dx = 1  # horizontal line
            else:
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                # Ensure consistent sign: make dx positive, or if dx==0 make dy positive
                if dx < 0:
                    dx = -dx
                    dy = -dy

            key = (dx, dy)
            slopes[key] = slopes.get(key, 0) + 1

        if slopes:
            best = max(best, max(slopes.values()) + 1)

    return best


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
