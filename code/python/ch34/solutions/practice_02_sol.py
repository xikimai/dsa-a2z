"""
Solution for Practice 2: Line Segment Intersection
====================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
For each pair of segments AB and CD:
1. Compute orientations d1=orientation(C,D,A), d2=orientation(C,D,B),
   d3=orientation(A,B,C), d4=orientation(A,B,D)
2. General case: segments cross if d1*d2 < 0 AND d3*d4 < 0
3. Special cases: check collinear points with on-segment test

TIME COMPLEXITY:  O(n) for n queries
SPACE COMPLEXITY: O(1) per query
"""


def solve(segments: list[list[list[int]]]) -> list[bool]:
    """Return True/False for each pair of segments."""
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def orientation(a, b, c):
        cp = cross(a, b, c)
        if cp > 0:
            return 1
        if cp < 0:
            return -1
        return 0

    def on_segment(p, q, r):
        """Check if q lies on segment pr (assuming collinear)."""
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

    def intersects(a, b, c, d):
        d1 = orientation(c, d, a)
        d2 = orientation(c, d, b)
        d3 = orientation(a, b, c)
        d4 = orientation(a, b, d)

        if d1 * d2 < 0 and d3 * d4 < 0:
            return True

        if d1 == 0 and on_segment(c, a, d):
            return True
        if d2 == 0 and on_segment(c, b, d):
            return True
        if d3 == 0 and on_segment(a, c, b):
            return True
        if d4 == 0 and on_segment(a, d, b):
            return True

        return False

    result = []
    for seg in segments:
        a, b, c, d = seg
        result.append(intersects(a, b, c, d))
    return result


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
