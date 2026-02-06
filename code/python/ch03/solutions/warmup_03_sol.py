"""
Solution for Warmup 03: Largest of Three
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use Python's built-in max() function. You could also chain if/elif/else
comparisons, but max() is cleaner and less error-prone.

TIME COMPLEXITY:  O(1) — comparing three values
SPACE COMPLEXITY: O(1) — no extra memory
"""


def solve(a: int, b: int, c: int) -> int:
    """Return the largest of three integers."""
    return max(a, b, c)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
