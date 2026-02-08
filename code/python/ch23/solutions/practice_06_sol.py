"""
Solution for Practice 6: Tribonacci Number
=============================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
T(n) = T(n-1) + T(n-2) + T(n-3). Space-optimized to three variables.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the nth Tribonacci number."""
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
