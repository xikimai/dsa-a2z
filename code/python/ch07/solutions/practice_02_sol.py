"""
Solution for Practice 2: GCD and LCM
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Euclidean algorithm: GCD(a, b) = GCD(b, a % b) until b == 0.
LCM = a // gcd * b (overflow-safe order).

TIME COMPLEXITY:  O(log(min(a,b)))
SPACE COMPLEXITY: O(1)
"""


def solve(a: int, b: int) -> list[int]:
    """Return [gcd, lcm] of a and b."""
    # Euclidean GCD
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    # LCM: a // gcd * b (avoid overflow)
    if gcd == 0:
        lcm = 0
    else:
        lcm = a // gcd * b
    return [gcd, lcm]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result[0], result[1])
