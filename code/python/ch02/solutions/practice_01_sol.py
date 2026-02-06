"""
Solution for Practice 01: Circle Properties
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use the formulas:
    area = pi * r^2
    circumference = 2 * pi * r

We use math.pi for an accurate value of pi. In Python, r**2 gives r
squared (the exponentiation operator).

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""

import math


def solve(radius: float) -> tuple[float, float]:
    """Return a tuple (area, circumference) for a circle with the given radius."""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return (area, circumference)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    radius = float(input())
    area, circumference = solve(radius)
    print(area)
    print(circumference)
