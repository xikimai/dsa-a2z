"""
Solution for Practice 02: Digit Count
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Handle the special case of n = 0 first (it has 1 digit). Then work with
the absolute value and repeatedly divide by 10, counting iterations
until the number becomes 0.

TIME COMPLEXITY:  O(d) — where d is the number of digits (at most 10)
SPACE COMPLEXITY: O(1) — just a counter variable
"""


def solve(n: int) -> int:
    """Return the number of digits in n."""
    if n == 0:
        return 1
    count = 0
    n = n if n > 0 else -n  # handle negatives without abs()
    while n > 0:
        n //= 10
        count += 1
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
