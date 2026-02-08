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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))

