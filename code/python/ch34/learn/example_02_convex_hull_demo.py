"""
Example 02: Convex Hull Demo — Step-by-Step Construction
========================================================
Chapter 34: Computational Geometry & Sweep Line

This example demonstrates Andrew's Monotone Chain convex hull
algorithm step by step, showing the lower hull and upper hull
construction.
"""


def cross(o, a, b):
    """Cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull_verbose(points):
    """Build convex hull with step-by-step output."""
    pts = sorted(set(map(tuple, points)))
    print(f"\n  Sorted unique points: {list(pts)}")

    if len(pts) <= 1:
        return [list(p) for p in pts]

    # Build lower hull
    print("\n  --- Building Lower Hull (left to right) ---")
    lower = []
    for p in pts:
        while len(lower) >= 2:
            cp = cross(lower[-2], lower[-1], p)
            if cp <= 0:
                removed = lower.pop()
                print(f"    Remove {list(removed)} (cross product = {cp}, not a left turn)")
            else:
                break
        lower.append(p)
        print(f"    Add {list(p)} -> lower = {[list(x) for x in lower]}")

    # Build upper hull
    print("\n  --- Building Upper Hull (right to left) ---")
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2:
            cp = cross(upper[-2], upper[-1], p)
            if cp <= 0:
                removed = upper.pop()
                print(f"    Remove {list(removed)} (cross product = {cp}, not a left turn)")
            else:
                break
        upper.append(p)
        print(f"    Add {list(p)} -> upper = {[list(x) for x in upper]}")

    # Combine
    hull = lower[:-1] + upper[:-1]
    return [list(p) for p in hull]


# ── Main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("CONVEX HULL: Andrew's Monotone Chain — Step by Step")
    print("=" * 60)

    # Example 1: Square with interior point
    points1 = [[0, 0], [2, 0], [2, 2], [0, 2], [1, 1]]
    print(f"\n  Input points: {points1}")
    hull1 = convex_hull_verbose(points1)
    print(f"\n  Convex hull (CCW): {hull1}")
    print(f"  Point (1,1) is interior — not on hull!")

    # Example 2: Triangle
    print("\n" + "=" * 60)
    points2 = [[0, 0], [4, 0], [2, 3]]
    print(f"\n  Input points: {points2}")
    hull2 = convex_hull_verbose(points2)
    print(f"\n  Convex hull (CCW): {hull2}")

    # Example 3: All collinear
    print("\n" + "=" * 60)
    points3 = [[0, 0], [1, 0], [2, 0], [3, 0]]
    print(f"\n  Input points: {points3}")
    hull3 = convex_hull_verbose(points3)
    print(f"\n  Convex hull (degenerate — collinear): {hull3}")

    # Example 4: Larger set
    print("\n" + "=" * 60)
    points4 = [[1, 1], [2, 5], [3, 3], [5, 3], [3, 2], [2, 2], [0, 3]]
    print(f"\n  Input points: {points4}")
    hull4 = convex_hull_verbose(points4)
    print(f"\n  Convex hull (CCW): {hull4}")
    print(f"  Interior points not on hull: (2,2), (3,2), (3,3)")
