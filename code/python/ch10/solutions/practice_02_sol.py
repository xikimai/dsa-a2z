"""
Solution for Practice 2: Sum of Digits
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Take absolute value first (handle negatives).
Base case: single digit (n < 10), return n.
Recursive case: last digit (n % 10) + sum of remaining digits (n // 10).

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(d) — recursion stack depth
"""


def solve(n: int) -> int:
    """Sum the digits of |n| recursively."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + solve(n // 10)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
