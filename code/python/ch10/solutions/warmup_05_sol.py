"""
Solution for Warmup 5: Power
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Base case: anything^0 = 1.
Recursive case: base * base^(exp-1).
This is O(exp) — one multiplication per step.

TIME COMPLEXITY:  O(exp)
SPACE COMPLEXITY: O(exp) — recursion stack depth
"""


def solve(base: int, exp: int) -> int:
    """Compute base^exp recursively in O(exp) time."""
    if exp == 0:
        return 1
    return base * solve(base, exp - 1)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    b, e = map(int, input().split())
    print(solve(b, e))
