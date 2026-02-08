"""
Solution for Warmup 4: Check if i-th Bit Is Set
=================================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
Right-shift n by i positions, then AND with 1.
If the result is 1, the bit is set.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int, i: int) -> bool:
    """Return True if the i-th bit of n is set."""
    return ((n >> i) & 1) == 1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, i = int(parts[0]), int(parts[1])
    print(solve(n, i))
