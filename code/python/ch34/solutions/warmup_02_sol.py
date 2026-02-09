"""
Solution for Warmup 2: Convex Hull
====================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
Andrew's Monotone Chain algorithm:
1. Sort points by (x, y)
2. Build lower hull (left to right, keeping left turns)
3. Build upper hull (right to left, keeping left turns)
4. Concatenate

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""


def solve(points: list[list[int]]) -> list[list[int]]:
    """Return convex hull vertices in CCW order."""
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    pts = sorted(set(map(tuple, points)))
    if len(pts) <= 1:
        return [list(p) for p in pts]

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
    return [list(p) for p in hull]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
