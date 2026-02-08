"""
Solution for Warmup 4: Count Binary Strings
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
DP / Fibonacci-like recurrence:
  ending_in_0[i] = ending_in_0[i-1] + ending_in_1[i-1]
  ending_in_1[i] = ending_in_0[i-1]  (can't have consecutive 1s)
Total = ending_in_0[n] + ending_in_1[n]
This is the (n+2)-th Fibonacci number.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return count of n-length binary strings with no consecutive 1s."""
    if n == 1:
        return 2
    # a = count ending in 0, b = count ending in 1
    a, b = 1, 1  # For n=1: "0" ends in 0, "1" ends in 1
    for _ in range(2, n + 1):
        a, b = a + b, a
    return a + b


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
