"""
Warmup 3: Count Vowels
==============================
Chapter 5: Collections

PROBLEM
-------
Count the number of vowels (a, e, i, o, u) in a string.
The count should be case-insensitive (both 'A' and 'a' count).

INPUT FORMAT
------------
A single line of text.

OUTPUT FORMAT
-------------
A single integer: the count of vowels.

CONSTRAINTS
-----------
- The string can be empty
- The string can contain any characters (letters, digits, punctuation)

EXAMPLES
--------
Input:  Hello World
Output: 3

Input:  aeiou
Output: 5

Input:  xyz
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> int:
    """Return the count of vowels in the string (case-insensitive)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
