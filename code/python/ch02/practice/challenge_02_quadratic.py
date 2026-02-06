"""
Challenge 02: Quadratic Discriminant
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given coefficients a, b, and c of a quadratic equation ax^2 + bx + c = 0,
compute the discriminant and determine the number of real roots.

The discriminant is:
    disc = b^2 - 4ac

Number of real roots:
    - 2 roots if disc > 0
    - 1 root  if disc == 0
    - 0 roots if disc < 0

INPUT FORMAT
------------
A single line containing three space-separated floats: a, b, c.

OUTPUT FORMAT
-------------
Print the discriminant (as a float) and the number of roots (as an integer),
separated by a space.

CONSTRAINTS
-----------
-10^3 <= a, b, c <= 10^3
a != 0

EXAMPLES
--------
Input:  1 -3 2
Output: 1.0 2

Input:  1 2 1
Output: 0.0 1

Input:  1 1 1
Output: -3.0 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: float, b: float, c: float) -> tuple[float, int]:
    """Return a tuple (discriminant, num_roots) for the quadratic ax^2 + bx + c = 0."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b, c = map(float, input().split())
    disc, num_roots = solve(a, b, c)
    print(disc, num_roots)
