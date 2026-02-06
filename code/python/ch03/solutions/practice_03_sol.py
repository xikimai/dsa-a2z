"""
Solution for Practice 03: Reverse Number
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Handle the sign separately. Then repeatedly extract the last digit
using % 10 and build the reversed number by multiplying the accumulator
by 10 and adding the digit. Leading zeros in the reversed result are
naturally dropped since we're working with integers.

TIME COMPLEXITY:  O(d) — where d is the number of digits
SPACE COMPLEXITY: O(1) — just the accumulator
"""


def solve(n: int) -> int:
    """Return the integer with its digits reversed."""
    sign = -1 if n < 0 else 1
    n = n if n >= 0 else -n
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return sign * reversed_n


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
