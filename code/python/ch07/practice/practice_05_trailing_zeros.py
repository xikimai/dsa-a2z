"""
Practice 5: Trailing Zeros in Factorial
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given a non-negative integer n, return the number of trailing zeros
in n! (n factorial).

Trailing zeros come from factors of 10, and each 10 = 2 * 5.
Since there are always more factors of 2 than 5 in n!, you just
need to count the factors of 5.

Count factors of 5 using: n//5 + n//25 + n//125 + ...

INPUT FORMAT
------------
A single non-negative integer n.

OUTPUT FORMAT
-------------
A single integer: the number of trailing zeros in n!.

CONSTRAINTS
-----------
- 0 <= n <= 10^9

EXAMPLES
--------
Input:
  5
Output: 1

Input:
  10
Output: 2

Input:
  25
Output: 6

Input:
  100
Output: 24

Input:
  0
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the number of trailing zeros in n!."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
