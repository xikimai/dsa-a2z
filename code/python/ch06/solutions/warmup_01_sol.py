"""
Solution for Warmup 1: Count the Steps
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a simple if/elif chain to map each code_id to its formula.
For "log_loop", use math.floor(math.log2(n)) when n >= 1.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""

import math


def solve(code_id: str, n: int) -> int:
    """Return the exact operation count for the given code pattern and n."""
    if code_id == "single_loop":
        return n
    elif code_id == "double_loop":
        return n * n
    elif code_id == "half_loop":
        return n // 2
    elif code_id == "dependent_loop":
        return n * (n + 1) // 2
    elif code_id == "log_loop":
        if n >= 1:
            return int(math.floor(math.log2(n)))
        return 0
    return 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    code_id = input().strip()
    n = int(input().strip())
    print(solve(code_id, n))
