"""
Solution for Challenge 1: Fibonacci Three Ways
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Three implementations showing the evolution of a solution:

1. solve_naive: Direct recursion. O(2^n) time — exponentially slow!
2. solve_memo:  Recursion + dict memoization. O(n) time, O(n) space.
3. solve_iter:  Iterative with two variables. O(n) time, O(1) space.

solve() delegates to solve_iter (the best approach).

TIME COMPLEXITY:  O(n) for solve_memo and solve_iter; O(2^n) for solve_naive
SPACE COMPLEXITY: O(1) for solve_iter; O(n) for others
"""


def solve_naive(n: int) -> int:
    """Fibonacci using pure recursion (no memo). O(2^n) — very slow!"""
    if n <= 1:
        return n
    return solve_naive(n - 1) + solve_naive(n - 2)


def solve_memo(n: int) -> int:
    """Fibonacci using recursion + memoization. O(n)."""
    memo = {}

    def fib(k):
        if k <= 1:
            return k
        if k in memo:
            return memo[k]
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return fib(n)


def solve_iter(n: int) -> int:
    """Fibonacci using iteration. O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def solve(n: int) -> int:
    """Default solver — uses the iterative approach."""
    return solve_iter(n)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
