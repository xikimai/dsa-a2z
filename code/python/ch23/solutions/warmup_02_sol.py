"""
Solution for Warmup 2: Fibonacci Number
==========================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Space-optimized bottom-up. F(n) = F(n-1) + F(n-2).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
