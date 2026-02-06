"""
Challenge 1: Prime Check
==============================
Chapter 4: Functions

PROBLEM
-------
Determine whether an integer n is prime.

You must implement THREE versions of the primality test as helper functions:
  - is_prime_v1(n): Check all divisors from 2 to n-1
  - is_prime_v2(n): Check divisors from 2 to sqrt(n)
  - is_prime_v3(n): Use the 6k +/- 1 optimization

The solve() function should call is_prime_v3.

The 6k +/- 1 optimization:
  All primes > 3 are of the form 6k +/- 1. So after checking 2 and 3,
  you only need to check divisors of the form 6k-1 and 6k+1 up to sqrt(n).

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
"True" or "False"

CONSTRAINTS
-----------
- n can be any integer (including 0, 1, negatives)
- n <= 10^9

EXAMPLES
--------
Input:  7
Output: True

Input:  1
Output: False

Input:  2
Output: True

Input:  15
Output: False

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def is_prime_v1(n: int) -> bool:
    """Check primality by testing all divisors from 2 to n-1."""
    pass  # TODO: Replace this with your solution


def is_prime_v2(n: int) -> bool:
    """Check primality by testing divisors from 2 to sqrt(n)."""
    pass  # TODO: Replace this with your solution


def is_prime_v3(n: int) -> bool:
    """Check primality using the 6k +/- 1 optimization."""
    pass  # TODO: Replace this with your solution


def solve(n: int) -> bool:
    """Return True if n is prime, using is_prime_v3."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
