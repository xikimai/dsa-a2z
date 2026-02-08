"""
Solution for Warmup 3: Check Power of Two
==========================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
A power of 2 has exactly one set bit. n & (n - 1) clears the lowest
set bit. If the result is 0 and n > 0, then n is a power of 2.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> bool:
    """Return True if n is a power of two."""
    return n > 0 and (n & (n - 1)) == 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
