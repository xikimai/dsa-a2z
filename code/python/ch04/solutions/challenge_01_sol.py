"""
Solution for Challenge 1: Prime Check
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Three progressively optimized versions:

v1 — Brute force: check all divisors from 2 to n-1.  O(n)
v2 — Square root:  check divisors from 2 to sqrt(n). O(sqrt(n))
v3 — 6k +/- 1:    after checking 2 and 3, only check numbers of
                   the form 6k-1 and 6k+1 up to sqrt(n). Still
                   O(sqrt(n)) but with ~3x fewer iterations.

Why 6k +/- 1 works: Every integer is of the form 6k, 6k+1, 6k+2,
6k+3, 6k+4, or 6k+5. Of these, 6k, 6k+2, 6k+4 are divisible by 2,
and 6k+3 is divisible by 3. So any prime > 3 must be 6k+1 or 6k+5
(which is the same as 6k-1 for the next k).

TIME COMPLEXITY:  O(sqrt(n))
SPACE COMPLEXITY: O(1)
"""


def is_prime_v1(n: int) -> bool:
    """Check primality by testing all divisors from 2 to n-1."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_v2(n: int) -> bool:
    """Check primality by testing divisors from 2 to sqrt(n)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_prime_v3(n: int) -> bool:
    """Check primality using the 6k +/- 1 optimization."""
    if n < 2:
        return False
    if n < 4:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solve(n: int) -> bool:
    """Return True if n is prime, using is_prime_v3."""
    return is_prime_v3(n)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
