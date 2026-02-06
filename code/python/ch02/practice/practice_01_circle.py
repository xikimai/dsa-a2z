"""
Practice 01: Circle Properties
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given the radius of a circle, compute its area and circumference.

Formulas:
    area = pi * r^2
    circumference = 2 * pi * r

Use math.pi for the value of pi.

INPUT FORMAT
------------
A single line containing a float — the radius.

OUTPUT FORMAT
-------------
Print two floats on separate lines: the area and the circumference.

CONSTRAINTS
-----------
0 < radius <= 10^4

EXAMPLES
--------
Input:  1.0
Output: 3.141592653589793
        6.283185307179586

Input:  5.0
Output: 78.53981633974483
        31.41592653589793

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(radius: float) -> tuple[float, float]:
    """Return a tuple (area, circumference) for a circle with the given radius."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    radius = float(input())
    area, circumference = solve(radius)
    print(area)
    print(circumference)
