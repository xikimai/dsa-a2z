"""
Solution for Warmup 5: Armstrong Number
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Count digits, then sum each digit raised to that power. Compare with original.

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    if n < 0:
        return False
    # Count digits
    num_digits = 0
    temp = n
    if n == 0:
        num_digits = 1
    else:
        while temp > 0:
            num_digits += 1
            temp //= 10
    # Sum of digits^num_digits
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    return total == n


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
