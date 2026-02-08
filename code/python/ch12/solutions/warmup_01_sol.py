"""
Solution for Warmup 1: Binary Representation
==============================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
Repeatedly divide n by 2, collecting remainders.
The remainders (read in reverse) form the binary string.

TIME COMPLEXITY:  O(log n) — number of bits in n
SPACE COMPLEXITY: O(log n) — for the result string
"""


def solve(n: int) -> str:
    """Return binary representation of n as a string (no built-in)."""
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
