"""
Solution for Warmup 02: Absolute Value
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
If n is negative, negate it to make it positive. Otherwise, return as-is.
This is exactly what the built-in abs() does under the hood.

TIME COMPLEXITY:  O(1) — just a comparison and possibly a negation
SPACE COMPLEXITY: O(1) — no extra memory
"""


def solve(n: int) -> int:
    """Return the absolute value of n without using abs()."""
    if n < 0:
        return -n
    return n


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
