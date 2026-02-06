"""
Practice 2: Password Strength
==============================
Chapter 4: Functions

PROBLEM
-------
Check the strength of a password:
  - "weak"   : fewer than 8 characters
  - "medium" : 8 or more characters AND contains at least one digit
  - "strong" : 8 or more characters AND contains at least one digit
               AND at least one uppercase letter

If the password is 8+ chars but has no digit, it's still "weak".
Define has_digit(s) and has_upper(s) helper functions.

INPUT FORMAT
------------
A single string: the password.

OUTPUT FORMAT
-------------
One of: "weak", "medium", "strong"

CONSTRAINTS
-----------
- Password can be any string (including empty)

EXAMPLES
--------
Input:  hello
Output: weak

Input:  hello123
Output: medium

Input:  Hello123
Output: strong

Input:  ABCDEFGH
Output: weak

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def has_digit(s: str) -> bool:
    """Return True if s contains at least one digit (0-9)."""
    pass  # TODO: Replace this with your solution


def has_upper(s: str) -> bool:
    """Return True if s contains at least one uppercase letter."""
    pass  # TODO: Replace this with your solution


def solve(password: str) -> str:
    """Return 'weak', 'medium', or 'strong' based on password strength."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    password = input()
    print(solve(password))
