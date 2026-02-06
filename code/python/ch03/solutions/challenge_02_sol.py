"""
Solution for Challenge 02: Prime Check
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
A prime must be > 1. Then check divisibility from 2 up to sqrt(n).
If any number in that range divides n, it's not prime. We only need
to check up to sqrt(n) because if n = a * b, then at least one of
a or b must be <= sqrt(n).

TIME COMPLEXITY:  O(sqrt(n)) — checking divisors up to sqrt(n)
SPACE COMPLEXITY: O(1) — no extra memory
"""


def solve(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
