"""
Solution for Warmup 4: Repeat String
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Create a list of n copies of s, then join them with spaces.
When n is 0, the list is empty and join returns "".

TIME COMPLEXITY:  O(n * len(s))
SPACE COMPLEXITY: O(n * len(s)) for the result string
"""


def solve(s: str, n: int = 3) -> str:
    """Return s repeated n times separated by spaces."""
    return " ".join([s] * n)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    n = int(input())
    print(solve(s, n))
