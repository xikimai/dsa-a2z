"""
Solution for Practice 1: Fibonacci
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Use recursion with a dictionary for memoization.
Base cases: F(0) = 0, F(1) = 1.
Before computing F(n), check if it's already in the memo dict.
After computing, store the result in the memo dict.

TIME COMPLEXITY:  O(n) — each value computed once
SPACE COMPLEXITY: O(n) — memo dict + recursion stack
"""


def solve(n: int) -> int:
    """Return the nth Fibonacci number using memoized recursion."""
    memo = {}

    def fib(k):
        if k <= 1:
            return k
        if k in memo:
            return memo[k]
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return fib(n)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
