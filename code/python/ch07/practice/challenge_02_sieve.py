"""
Challenge 2: Sieve of Eratosthenes
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given a non-negative integer n, return a list of all prime numbers
less than or equal to n, in ascending order.

Use the Sieve of Eratosthenes algorithm:
1. Create a boolean list of size n+1, initially all True.
2. Mark 0 and 1 as not prime.
3. For each number i starting from 2, if it is still marked prime,
   mark all its multiples (starting from i*i) as not prime.
4. Collect all numbers still marked as prime.

If n < 2, return an empty list.

INPUT FORMAT
------------
A single non-negative integer n.

OUTPUT FORMAT
-------------
A single line of space-separated primes <= n.

CONSTRAINTS
-----------
- 0 <= n <= 10^7

EXAMPLES
--------
Input:
  10
Output: 2 3 5 7

Input:
  30
Output: 2 3 5 7 11 13 17 19 23 29

Input:
  1
Output: (empty)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[int]:
    """Return all primes <= n using the Sieve of Eratosthenes."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
