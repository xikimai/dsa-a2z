"""
Warmup 03: Celsius to Fahrenheit
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given a temperature in Celsius, convert it to Fahrenheit using the formula:
    F = C * 9/5 + 32

INPUT FORMAT
------------
A single line containing a float — the temperature in Celsius.

OUTPUT FORMAT
-------------
Print the temperature in Fahrenheit as a float.

CONSTRAINTS
-----------
-273.15 <= celsius <= 10^6

EXAMPLES
--------
Input:  0.0
Output: 32.0

Input:  100.0
Output: 212.0

Input:  -40.0
Output: -40.0

Input:  37.0
Output: 98.6

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(celsius: float) -> float:
    """Convert Celsius to Fahrenheit and return the result."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    celsius = float(input())
    print(solve(celsius))
