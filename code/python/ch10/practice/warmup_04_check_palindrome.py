"""
Warmup 4: Check Palindrome
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Check whether a string is a palindrome using recursion.
A palindrome reads the same forwards and backwards (e.g., "racecar", "aba").

INPUT FORMAT
------------
A single line containing the string to check.

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 0 <= len(s) <= 1000
- The string contains only lowercase English letters.

EXAMPLES
--------
Input:
  racecar
Output: True

Input:
  hello
Output: False

Input:
  a
Output: True

HINT
----
Base case: strings of length 0 or 1 are always palindromes.
Compare the first and last characters. If they differ, return False.
Otherwise, recursively check the middle substring s[1:-1].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> bool:
    """Check if the string is a palindrome, recursively."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
