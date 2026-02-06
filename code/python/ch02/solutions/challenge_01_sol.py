"""
Solution for Challenge 01: Extract Digits
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use integer division and modulo to extract each digit:
    hundreds = n // 100       (removes last two digits)
    tens     = (n // 10) % 10 (removes last digit, then takes last digit)
    ones     = n % 10         (takes last digit)

This is a pure math approach — no strings involved! Understanding how
// and % work together to extract digits is a fundamental CP skill.

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(n: int) -> tuple[int, int, int]:
    """Return a tuple (hundreds, tens, ones) for a 3-digit number n."""
    hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10
    return (hundreds, tens, ones)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    h, t, o = solve(n)
    print(h, t, o)
