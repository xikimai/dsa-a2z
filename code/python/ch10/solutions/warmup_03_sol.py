"""
Solution for Warmup 3: Reverse String
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Base case: a string of length 0 or 1 is already reversed.
Recursive case: reverse everything after the first character,
then append the first character at the end.

TIME COMPLEXITY:  O(n^2) — string concatenation at each level
SPACE COMPLEXITY: O(n) — recursion depth + string copies
"""


def solve(s: str) -> str:
    """Reverse a string using recursion."""
    if len(s) <= 1:
        return s
    return solve(s[1:]) + s[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
