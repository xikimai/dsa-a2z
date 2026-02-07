"""
Solution for Warmup 4: Palindrome Number
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Negative numbers are not palindromes. Reverse the number and compare.

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> bool:
    """Return True if n is a palindrome number."""
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
