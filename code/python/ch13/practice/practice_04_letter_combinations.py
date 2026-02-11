"""
Practice 4: Letter Combinations of a Phone Number
===================================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a string of digits (2-9), return all possible letter combinations
that the digits could represent on a phone keypad. Mapping:
2=abc, 3=def, 4=ghi, 5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz.

INPUT FORMAT
------------
A single string of digits (2-9). May be empty.

OUTPUT FORMAT
-------------
Each combination on its own line. Empty list if input is empty.

CONSTRAINTS
-----------
- 0 <= len(digits) <= 4
- Each character is a digit from '2' to '9'

EXAMPLES
--------
Input:
  23
Output:
  ad
  ae
  af
  bd
  be
  bf
  cd
  ce
  cf

Input:
  2
Output:
  a
  b
  c

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(digits: str) -> list[str]:
    """Return all letter combinations for the given digits."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    digits = input().strip()
    result = solve(digits)
    for combo in result:
        print(combo)

