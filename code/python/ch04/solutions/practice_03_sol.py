"""
Solution for Practice 3: Temperature Converter
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Define c_to_f and f_to_c helper functions using the standard formulas.
In solve, check for valid units, handle same-unit case, then dispatch
to the correct converter. Round to 1 decimal place.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def c_to_f(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def solve(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between units. Return -1.0 for invalid units."""
    valid_units = {"C", "F"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return -1.0
    if from_unit == to_unit:
        return round(value, 1)
    if from_unit == "C" and to_unit == "F":
        return round(c_to_f(value), 1)
    return round(f_to_c(value), 1)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    value = float(input())
    from_unit = input().strip()
    to_unit = input().strip()
    print(solve(value, from_unit, to_unit))
