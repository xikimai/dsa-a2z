"""
Solution for Challenge 2: Performance Showdown
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Map each complexity string to its numeric operation count at size n,
then compare the two counts.  Use a helper function to avoid repeating
the mapping logic.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""

import math


def _ops(complexity: str, n: int) -> float:
    """Compute the number of operations for a complexity at size n."""
    if complexity == "1":
        return 1
    elif complexity == "log_n":
        return math.log2(n) if n > 0 else 0
    elif complexity == "n":
        return n
    elif complexity == "n_log_n":
        return n * math.log2(n) if n > 0 else 0
    elif complexity == "n^2":
        return n * n
    elif complexity == "n^3":
        return n * n * n
    elif complexity == "2^n":
        if n > 60:
            return float("inf")
        return 2**n
    return 0


def solve(complexity_a: str, complexity_b: str, n: int) -> str:
    """Return 'A', 'B', or 'TIE' based on which complexity is faster at n."""
    ops_a = _ops(complexity_a, n)
    ops_b = _ops(complexity_b, n)

    if ops_a < ops_b:
        return "A"
    elif ops_b < ops_a:
        return "B"
    else:
        return "TIE"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    complexity_a = parts[0]
    complexity_b = parts[1]
    n = int(parts[2])
    print(solve(complexity_a, complexity_b, n))
