"""
Solution for Warmup 2: Is It Fast Enough?
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Map each complexity string to its operation count at size n, then check
whether ops < 10^8.  For "2^n", bail early when n > 30 to avoid
computing a huge number.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""

import math

LIMIT = 10**8


def solve(n: int, complexity: str) -> bool:
    """Return True if the algorithm finishes within 10^8 operations."""
    if complexity == "1":
        ops = 1
    elif complexity == "log_n":
        ops = math.log2(n)
    elif complexity == "n":
        ops = n
    elif complexity == "n_log_n":
        ops = n * math.log2(n)
    elif complexity == "n^2":
        ops = n * n
    elif complexity == "n^3":
        ops = n * n * n
    elif complexity == "2^n":
        if n > 30:
            return False
        ops = 2**n
    else:
        ops = 0

    return ops < LIMIT


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    n = int(parts[0])
    complexity = parts[1]
    print(solve(n, complexity))
