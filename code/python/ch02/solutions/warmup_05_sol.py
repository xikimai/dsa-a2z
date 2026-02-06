"""
Solution for Warmup 05: Last Digit
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Take the absolute value of n first (to handle negatives), then use
modulo 10 to extract the last digit. The % operator gives the remainder
when dividing by 10, which is always the ones digit.

TIME COMPLEXITY:  O(1) — just two operations
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(n: int) -> int:
    """Return the last digit of n (always non-negative)."""
    return abs(n) % 10


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
