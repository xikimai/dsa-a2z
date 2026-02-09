"""
Solution for Practice 1: Closest Pair of Points
=================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
Divide and conquer:
1. Sort points by x-coordinate
2. Split into left and right halves
3. Recursively find closest pair in each half
4. Check strip of points near the dividing line
5. In the strip, each point only needs to be compared with ~6 others

TIME COMPLEXITY:  O(n log^2 n)
SPACE COMPLEXITY: O(n)
"""

import math


def solve(points: list[list[int]]) -> float:
    """Return distance between closest pair of points."""
    pts = sorted(points)

    def dist(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def rec(pts):
        n = len(pts)
        if n <= 3:
            best = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    best = min(best, dist(pts[i], pts[j]))
            return best

        mid = n // 2
        mid_x = pts[mid][0]
        d = min(rec(pts[:mid]), rec(pts[mid:]))

        # Build strip
        strip = [p for p in pts if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < d:
                d = min(d, dist(strip[i], strip[j]))
                j += 1

        return d

    return rec(pts)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
