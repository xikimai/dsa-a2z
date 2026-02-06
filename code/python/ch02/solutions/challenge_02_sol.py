"""
Solution for Challenge 02: Quadratic Discriminant
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Compute the discriminant using the formula:
    disc = b^2 - 4ac

Then determine the number of real roots:
    disc > 0  → 2 distinct real roots
    disc == 0 → 1 repeated real root
    disc < 0  → 0 real roots (complex roots)

This is a direct application of the quadratic formula from algebra.
The discriminant tells you everything about the nature of the roots
without actually computing them.

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(a: float, b: float, c: float) -> tuple[float, int]:
    """Return a tuple (discriminant, num_roots) for the quadratic ax^2 + bx + c = 0."""
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        num_roots = 2
    elif disc == 0:
        num_roots = 1
    else:
        num_roots = 0
    return (disc, num_roots)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b, c = map(float, input().split())
    disc, num_roots = solve(a, b, c)
    print(disc, num_roots)
