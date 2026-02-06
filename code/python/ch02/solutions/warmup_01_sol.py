"""
Solution for Warmup 01: Greeting
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use an f-string (or string concatenation) to build the greeting message.
This is the simplest possible string formatting exercise.

TIME COMPLEXITY:  O(n) — where n is the length of the name string
SPACE COMPLEXITY: O(n) — the new string we create
"""


def solve(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    name = input()
    print(solve(name))
