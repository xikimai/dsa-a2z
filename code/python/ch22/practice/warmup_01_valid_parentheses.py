"""
Warmup 1: Valid Parentheses
==============================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given a string containing only the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
  1. Open brackets are closed by the same type of brackets.
  2. Open brackets are closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

INPUT FORMAT
------------
A single string of bracket characters.

OUTPUT FORMAT
-------------
True if valid, False otherwise.

CONSTRAINTS
-----------
- 0 <= len(s) <= 10^4
- s consists of parentheses only: '(){}[]'

EXAMPLES
--------
Input: "()"
Output: True

Input: "([)]"
Output: False

Input: "{[]}"
Output: True

Input: ""
Output: True

HINT
----
Use a stack: push opening brackets, pop on closing, check for match.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> bool:
    """Return True if brackets are balanced."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
