"""
Warmup 01: Greeting
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given a person's name, produce a friendly greeting.

INPUT FORMAT
------------
A single line containing a string (the person's name).

OUTPUT FORMAT
-------------
Print "Hello, <name>!" where <name> is the input string.

CONSTRAINTS
-----------
1 <= len(name) <= 100
Name contains only letters and spaces.

EXAMPLES
--------
Input:  Maya
Output: Hello, Maya!

Input:  World
Output: Hello, World!

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
