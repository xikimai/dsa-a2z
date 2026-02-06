"""
Practice 02: Time Conversion
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given a total number of seconds, convert it to hours, minutes, and seconds.

For example, 3661 seconds = 1 hour, 1 minute, and 1 second.

INPUT FORMAT
------------
A single line containing a non-negative integer — total seconds.

OUTPUT FORMAT
-------------
Print three space-separated integers: hours, minutes, seconds.

CONSTRAINTS
-----------
0 <= total_seconds <= 86400

EXAMPLES
--------
Input:  3661
Output: 1 1 1

Input:  0
Output: 0 0 0

Input:  86399
Output: 23 59 59

Input:  45
Output: 0 0 45

Input:  3600
Output: 1 0 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(total_seconds: int) -> tuple[int, int, int]:
    """Return a tuple (hours, minutes, seconds) from the given total seconds."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    total_seconds = int(input())
    h, m, s = solve(total_seconds)
    print(h, m, s)
