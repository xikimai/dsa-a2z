"""
Solution for Practice 4: Letter Combinations of a Phone Number
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Backtrack: for each digit, try all its mapped letters and recurse.

TIME COMPLEXITY:  O(4^n) — each digit maps to at most 4 letters
SPACE COMPLEXITY: O(n) — recursion depth
"""


def solve(digits: str) -> list[str]:
    """Return all letter combinations for the given digits."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    digits = input().strip()
    result = solve(digits)
    for combo in result:
        print(combo)

