"""
Warmup 3: Reverse String
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Reverse a string using recursion. Do not use slicing tricks like s[::-1]
as your entire solution — build the reversal through recursive calls.

INPUT FORMAT
------------
A single line containing the string to reverse.

OUTPUT FORMAT
-------------
The reversed string.

CONSTRAINTS
-----------
- 0 <= len(s) <= 1000

EXAMPLES
--------
Input:
  hello
Output: olleh

Input:
  a
Output: a

Input:
  abcd
Output: dcba

HINT
----
Base case: a string of length 0 or 1 is already reversed.
Recursive case: reverse everything after the first character, then
append the first character at the end.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> str:
    """Reverse a string using recursion."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
