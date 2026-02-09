"""
Example 01: Geometry Basics — Cross Product, Distance, Orientation
==================================================================
Chapter 34: Computational Geometry & Sweep Line

This example demonstrates the fundamental building blocks of
computational geometry: vectors, cross product, dot product,
distance, and orientation testing.
"""

import math


# ── Cross Product ────────────────────────────────────────────

def cross(o, a, b):
    """Cross product of vectors OA and OB.
    Returns positive if counter-clockwise, negative if clockwise, 0 if collinear.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


# ── Dot Product ──────────────────────────────────────────────

def dot(o, a, b):
    """Dot product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[0] - o[0]) + (a[1] - o[1]) * (b[1] - o[1])


# ── Distance ─────────────────────────────────────────────────

def distance(a, b):
    """Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def distance_sq(a, b):
    """Squared Euclidean distance (avoid sqrt for comparisons)."""
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# ── Orientation ──────────────────────────────────────────────

def orientation(a, b, c):
    """Determine orientation of triplet (a, b, c).
    Returns:
         1  = counter-clockwise (left turn)
        -1  = clockwise (right turn)
         0  = collinear
    """
    cp = cross(a, b, c)
    if cp > 0:
        return 1
    if cp < 0:
        return -1
    return 0


# ── Main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("GEOMETRY BASICS: Cross Product, Distance, Orientation")
    print("=" * 60)

    # Cross product demo
    print("\n--- Cross Product ---")
    o = [0, 0]
    a = [4, 4]
    b = [1, 2]
    print(f"  O={o}, A={a}, B={b}")
    print(f"  cross(O, A, B) = {cross(o, a, b)}")  # 4*2 - 4*1 = 4 (positive = CCW)

    b2 = [1, 0]
    print(f"  O={o}, A={a}, B={b2}")
    print(f"  cross(O, A, B) = {cross(o, a, b2)}")  # 4*0 - 4*1 = -4 (negative = CW)

    b3 = [2, 2]
    print(f"  O={o}, A={a}, B={b3}")
    print(f"  cross(O, A, B) = {cross(o, a, b3)}")  # 4*2 - 4*2 = 0 (collinear)

    # Orientation demo
    print("\n--- Orientation ---")
    labels = {1: "Counter-Clockwise", -1: "Clockwise", 0: "Collinear"}
    for c_point, name in [([1, 2], "C=(1,2)"), ([1, 0], "C=(1,0)"), ([2, 2], "C=(2,2)")]:
        result = orientation([0, 0], [4, 4], c_point)
        print(f"  A=(0,0) B=(4,4) {name}: {labels[result]}")

    # Distance demo
    print("\n--- Distance ---")
    p1 = [0, 0]
    p2 = [3, 4]
    print(f"  distance({p1}, {p2}) = {distance(p1, p2)}")  # 5.0
    print(f"  distance_sq({p1}, {p2}) = {distance_sq(p1, p2)}")  # 25

    # Dot product demo
    print("\n--- Dot Product ---")
    print(f"  dot((0,0), (1,0), (0,1)) = {dot([0,0], [1,0], [0,1])}")  # 0 (perpendicular)
    print(f"  dot((0,0), (1,1), (2,2)) = {dot([0,0], [1,1], [2,2])}")  # 4 (same direction)
    print(f"  dot((0,0), (1,0), (-1,0)) = {dot([0,0], [1,0], [-1,0])}")  # -1 (opposite)
