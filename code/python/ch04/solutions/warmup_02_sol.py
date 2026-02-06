"""
Solution for Warmup 2: Power
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a loop to multiply base by itself exponent times. Start with result = 1
and multiply by base in each iteration.

TIME COMPLEXITY:  O(exponent)
SPACE COMPLEXITY: O(1)
"""


def solve(base: int, exponent: int) -> int:
    """Compute base^exponent using a loop (no built-in pow or **)."""
    result = 1
    for _ in range(exponent):
        result *= base
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    base = int(input())
    exponent = int(input())
    print(solve(base, exponent))
