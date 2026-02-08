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
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    results = []

    def backtrack(index, current):
        if index == len(digits):
            results.append(current)
            return
        for letter in mapping[digits[index]]:
            backtrack(index + 1, current + letter)

    backtrack(0, "")
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    digits = input().strip()
    result = solve(digits)
    for combo in result:
        print(combo)
