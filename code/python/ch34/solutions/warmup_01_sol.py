"""
Solution for Warmup 1: Cross Product and Orientation
=====================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
For each triplet (A, B, C), compute the cross product of vectors AB and AC.
The sign tells the orientation.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) per query
"""


def solve(queries: list[list[list[int]]]) -> list[int]:
    """Return orientation for each triplet of points."""
    result = []
    for q in queries:
        a, b, c = q
        # Cross product of AB x AC
        cp = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if cp > 0:
            result.append(1)   # counter-clockwise
        elif cp < 0:
            result.append(-1)  # clockwise
        else:
            result.append(0)   # collinear
    return result


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
