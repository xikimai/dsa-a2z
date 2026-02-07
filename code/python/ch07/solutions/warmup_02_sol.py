"""
Solution for Warmup 2: Reverse a Number
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Handle sign separately. Build reversed number using mod-10/div-10 pattern.

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the reversed number."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
