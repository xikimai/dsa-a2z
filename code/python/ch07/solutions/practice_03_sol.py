"""
Solution for Practice 3: Modular Exponentiation
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Binary exponentiation: square the base and halve the exponent each step.
If exponent is odd, multiply result by current base.

TIME COMPLEXITY:  O(log exp)
SPACE COMPLEXITY: O(1)
"""


def solve(base: int, exp: int, mod: int) -> int:
    """Return base^exp mod m using binary exponentiation."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    base, exp, mod = map(int, input().split())
    print(solve(base, exp, mod))
