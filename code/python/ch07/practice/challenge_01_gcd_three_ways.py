"""
Challenge 1: GCD Three Ways
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Implement the Greatest Common Divisor (GCD) using three different algorithms:

1. **Subtraction method** (solve_subtract): Repeatedly subtract the smaller
   number from the larger until they are equal. That value is the GCD.
   If either input is 0, the GCD is the other number.

2. **Euclidean algorithm** (solve_euclidean): Replace (a, b) with (b, a % b)
   until b is 0. Then a is the GCD. Much faster than subtraction!

3. **Extended Euclidean** (solve_extended): Returns [gcd, x, y] such that
   a*x + b*y = gcd(a, b). These coefficients (x, y) are called Bezout
   coefficients and are useful in cryptography and modular arithmetic.

Also implement solve(a, b) which returns the GCD using the Euclidean method.

INPUT FORMAT
------------
Two space-separated non-negative integers a and b.

OUTPUT FORMAT
-------------
A single integer: gcd(a, b).

CONSTRAINTS
-----------
- 0 <= a, b <= 10^9

EXAMPLES
--------
Input:
  48 18
Output: 6

Input:
  7 13
Output: 1

Input:
  0 5
Output: 5

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_subtract(a: int, b: int) -> int:
    """GCD by repeated subtraction. O(max(a,b))."""
    pass  # TODO: Replace this with your solution


def solve_euclidean(a: int, b: int) -> int:
    """GCD by Euclidean algorithm. O(log(min(a,b)))."""
    pass  # TODO: Replace this with your solution


def solve_extended(a: int, b: int) -> list[int]:
    """Extended Euclidean: returns [gcd, x, y] where a*x + b*y = gcd."""
    pass  # TODO: Replace this with your solution


def solve(a: int, b: int) -> int:
    """Default GCD — uses Euclidean algorithm."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))
