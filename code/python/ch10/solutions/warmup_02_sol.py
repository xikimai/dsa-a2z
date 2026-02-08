"""
Solution for Warmup 2: Sum of First N
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Base case: sum of first 0 numbers is 0.
Recursive case: n + sum(1..n-1).

TIME COMPLEXITY:  O(n) — one call per decrement
SPACE COMPLEXITY: O(n) — recursion stack depth
"""


def solve(n: int) -> int:
    """Compute 1 + 2 + ... + n recursively."""
    if n == 0:
        return 0
    return n + solve(n - 1)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
