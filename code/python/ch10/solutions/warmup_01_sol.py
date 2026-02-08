"""
Solution for Warmup 1: Factorial
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Classic recursion: the base case is 0! = 1.
For n > 0, return n * factorial(n - 1).

TIME COMPLEXITY:  O(n) — one recursive call per decrement
SPACE COMPLEXITY: O(n) — recursion stack depth
"""


def solve(n: int) -> int:
    """Compute n! recursively."""
    if n == 0:
        return 1
    return n * solve(n - 1)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
