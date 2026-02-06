"""
Practice 3: Temperature Converter
==============================
Chapter 4: Functions

PROBLEM
-------
Convert a temperature between Celsius and Fahrenheit.
Define c_to_f(c) and f_to_c(f) helper functions.

Formulas:
  F = C * 9/5 + 32
  C = (F - 32) * 5/9

Round the result to 1 decimal place.
If from_unit and to_unit are the same, return the value unchanged (still
rounded to 1 decimal).
If either unit is invalid (not "C" or "F"), return -1.0.

INPUT FORMAT
------------
Three values on separate lines: float value, string from_unit, string to_unit.

OUTPUT FORMAT
-------------
A float rounded to 1 decimal place.

CONSTRAINTS
-----------
- Units are "C" or "F" (uppercase)
- Value can be any float

EXAMPLES
--------
Input:  100.0, C, F
Output: 212.0

Input:  32.0, F, C
Output: 0.0

Input:  100.0, C, C
Output: 100.0

Input:  100.0, C, K
Output: -1.0

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def c_to_f(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    pass  # TODO: Replace this with your solution


def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    pass  # TODO: Replace this with your solution


def solve(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between units. Return -1.0 for invalid units."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    value = float(input())
    from_unit = input().strip()
    to_unit = input().strip()
    print(solve(value, from_unit, to_unit))
