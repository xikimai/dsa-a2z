"""
Solution for Practice 5: Trailing Zeros in Factorial
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Count factors of 5 in n!: n//5 + n//25 + n//125 + ...

TIME COMPLEXITY:  O(log_5(n))
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the number of trailing zeros in n!."""
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
