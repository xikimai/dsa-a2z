"""
Solution for Practice 3: Point in Polygon
==========================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
For each query point:
1. Check if the point lies on any edge (boundary check)
2. Ray casting: cast a ray rightward and count boundary crossings
   - Odd crossings = inside, even crossings = outside

TIME COMPLEXITY:  O(q * n) where q = queries, n = polygon vertices
SPACE COMPLEXITY: O(1) per query
"""


def solve(polygon: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """Return True/False for each query point."""
    n = len(polygon)

    def point_in_poly(px, py):
        # Check if on boundary
        for i in range(n):
            j = (i + 1) % n
            ax, ay = polygon[i]
            bx, by = polygon[j]
            # Cross product to check collinearity
            cp = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
            if cp == 0:
                if (min(ax, bx) <= px <= max(ax, bx) and
                        min(ay, by) <= py <= max(ay, by)):
                    return True

        # Ray casting
        inside = False
        j = n - 1
        for i in range(n):
            yi, yj = polygon[i][1], polygon[j][1]
            xi, xj = polygon[i][0], polygon[j][0]
            if (yi > py) != (yj > py):
                x_intersect = (xj - xi) * (py - yi) / (yj - yi) + xi
                if px < x_intersect:
                    inside = not inside
            j = i

        return inside

    return [point_in_poly(q[0], q[1]) for q in queries]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data["polygon"], data["queries"])))
