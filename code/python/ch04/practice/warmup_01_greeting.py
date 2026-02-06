"""
Warmup 1: Greeting
==============================
Chapter 4: Functions

PROBLEM
-------
Write a function that takes a person's name and returns a greeting string.

INPUT FORMAT
------------
A single string: the person's name.

OUTPUT FORMAT
-------------
A string in the format "Hello, {name}!"

CONSTRAINTS
-----------
- name can be any string, including an empty string

EXAMPLES
--------
Input:  Alice
Output: Hello, Alice!

Input:  (empty string)
Output: Hello, !

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(name: str) -> str:
    """Return a greeting string for the given name."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    name = input()
    print(solve(name))
