"""
Solution for Warmup 01: Even or Odd
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use the modulo operator (%) to check if n is divisible by 2.
If n % 2 == 0, the number is even; otherwise it's odd.

TIME COMPLEXITY:  O(1) — just one modulo operation
SPACE COMPLEXITY: O(1) — no extra memory
"""


def solve(n: int) -> str:
    """Return 'Even' if n is even, 'Odd' if n is odd."""
    return "Even" if n % 2 == 0 else "Odd"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
