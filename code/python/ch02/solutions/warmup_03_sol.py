"""
Solution for Warmup 03: Celsius to Fahrenheit
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Apply the conversion formula: F = C * 9/5 + 32.
Note that 9/5 in Python gives 1.8 (true division), which is what we want.

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(celsius: float) -> float:
    """Convert Celsius to Fahrenheit and return the result."""
    return celsius * 9 / 5 + 32


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    celsius = float(input())
    print(solve(celsius))
