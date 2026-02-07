"""
Practice 2: GCD and LCM
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given two non-negative integers a and b, return a list [gcd, lcm] where:
  - gcd is the Greatest Common Divisor of a and b
  - lcm is the Least Common Multiple of a and b

Use the Euclidean algorithm to compute GCD.
Compute LCM using the formula: lcm(a, b) = a // gcd * b
(divide first to avoid potential overflow in other languages).

If both a and b are 0, gcd is 0 and lcm is 0.
If one of them is 0, gcd is the other number and lcm is 0.

INPUT FORMAT
------------
Two space-separated integers a and b.

OUTPUT FORMAT
-------------
Two space-separated integers: gcd and lcm.

CONSTRAINTS
-----------
- 0 <= a, b <= 10^9

EXAMPLES
--------
Input:
  12 18
Output: 6 36

Input:
  7 13
Output: 1 91

Input:
  0 5
Output: 5 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: int, b: int) -> list[int]:
    """Return [gcd, lcm] of a and b."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result[0], result[1])
