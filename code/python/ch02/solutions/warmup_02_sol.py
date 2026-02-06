"""
Solution for Warmup 02: Rectangle Area
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Multiply length by width. The area of a rectangle is simply length * width.

TIME COMPLEXITY:  O(1) — just one multiplication
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(length: int, width: int) -> int:
    """Return the area of a rectangle with the given length and width."""
    return length * width


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    length, width = map(int, input().split())
    print(solve(length, width))
