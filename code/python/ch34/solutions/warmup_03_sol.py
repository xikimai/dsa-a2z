"""
Solution for Warmup 3: Polygon Area (Shoelace Formula)
=======================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
Shoelace formula: Area = |sum(x_i * y_{i+1} - x_{i+1} * y_i)| / 2

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(polygon: list[list[int]]) -> float:
    """Return the area of a simple polygon."""
    n = len(polygon)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
