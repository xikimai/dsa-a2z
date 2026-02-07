"""
Practice 4: Prime Factorization
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given a positive integer n, return its prime factorization as a list
of [prime, count] pairs, sorted by prime in ascending order.

Use trial division: check each potential factor from 2 up to sqrt(n).
If a factor divides n, count how many times it divides and record
[factor, count]. If n > 1 after the loop, n itself is prime.

If n is 1, return an empty list (1 has no prime factors).

INPUT FORMAT
------------
A single positive integer n.

OUTPUT FORMAT
-------------
Space-separated entries of the form "prime^count".

CONSTRAINTS
-----------
- 1 <= n <= 10^9

EXAMPLES
--------
Input:
  12
Output: 2^2 3^1

Input:
  7
Output: 7^1

Input:
  360
Output: 2^3 3^2 5^1

Input:
  1
Output: (empty)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[list[int]]:
    """Return prime factorization as [[prime, count], ...] sorted by prime."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    for prime, count in result:
        print(f"{prime}^{count}", end=" ")
    print()
