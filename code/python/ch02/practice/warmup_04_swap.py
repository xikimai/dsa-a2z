"""
Warmup 04: Swap Two Numbers
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given two integers a and b, return them in swapped order.

INPUT FORMAT
------------
A single line containing two space-separated integers: a and b.

OUTPUT FORMAT
-------------
Print two space-separated integers: b and a (swapped).

CONSTRAINTS
-----------
-10^6 <= a, b <= 10^6

EXAMPLES
--------
Input:  3 7
Output: 7 3

Input:  0 0
Output: 0 0

Input:  -1 1
Output: 1 -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: int, b: int) -> tuple[int, int]:
    """Return a tuple with a and b swapped."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result[0], result[1])
