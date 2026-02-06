"""
Solution for Warmup 01: Sum of Two Numbers
============================================
Chapter 1: The Coder's Toolkit

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Simply return a + b. No tricks needed for this one — the goal is to
practice the workflow: read input, compute, print output.

TIME COMPLEXITY:  O(1) — just one addition
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))
