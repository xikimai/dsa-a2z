"""
Solution for Warmup 1: Greeting
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use an f-string to format the name into the greeting template.

TIME COMPLEXITY:  O(n) where n = len(name)
SPACE COMPLEXITY: O(n) for the new string
"""


def solve(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    name = input()
    print(solve(name))
