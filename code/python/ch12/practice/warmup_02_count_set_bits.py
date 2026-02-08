"""
Solution for Warmup 2: Count Set Bits
======================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
Brian Kernighan's algorithm: n &= (n - 1) clears the lowest set bit.
Loop until n becomes 0, counting iterations.

TIME COMPLEXITY:  O(k) where k = number of set bits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the number of set bits in n."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))

