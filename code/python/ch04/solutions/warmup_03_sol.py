"""
Solution for Warmup 3: Min of Three
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Define a helper min_of_two that returns the smaller of two values.
Then use it twice: first compare a and b, then compare that result with c.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def min_of_two(a: int, b: int) -> int:
    """Return the smaller of a and b."""
    if a <= b:
        return a
    return b


def solve(a: int, b: int, c: int) -> int:
    """Return the minimum of a, b, and c using min_of_two."""
    return min_of_two(min_of_two(a, b), c)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(a, b, c))
