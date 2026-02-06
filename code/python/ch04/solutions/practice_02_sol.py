"""
Solution for Practice 2: Password Strength
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Define has_digit and has_upper helper functions that loop through the
string checking each character. Then use length and these helpers to
classify the password strength.

TIME COMPLEXITY:  O(n) where n = len(password)
SPACE COMPLEXITY: O(1)
"""


def has_digit(s: str) -> bool:
    """Return True if s contains at least one digit (0-9)."""
    for ch in s:
        if ch.isdigit():
            return True
    return False


def has_upper(s: str) -> bool:
    """Return True if s contains at least one uppercase letter."""
    for ch in s:
        if ch.isupper():
            return True
    return False


def solve(password: str) -> str:
    """Return 'weak', 'medium', or 'strong' based on password strength."""
    if len(password) < 8 or not has_digit(password):
        return "weak"
    if has_upper(password):
        return "strong"
    return "medium"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    password = input()
    print(solve(password))
