"""
Solution for Practice 4: Custom Comparator
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Use Python's sorted() with a tuple key: (len(word), word). This sorts
primarily by length (ascending) and breaks ties alphabetically.

TIME COMPLEXITY:  O(n log n) where n is the number of words
SPACE COMPLEXITY: O(n)
"""


def solve(words: list[str]) -> list[str]:
    """Sort strings by length ascending, then alphabetically for ties."""
    return sorted(words, key=lambda w: (len(w), w))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = input().split()
    print(*solve(data))
