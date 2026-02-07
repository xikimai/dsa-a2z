"""
Practice 4: Custom Comparator
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Sort a list of strings by length in ascending order. If two strings have
the same length, sort them alphabetically (lexicographically).

INPUT FORMAT
------------
A single line of space-separated words.

OUTPUT FORMAT
-------------
A single line of space-separated words, sorted by the rules above.

CONSTRAINTS
-----------
- 0 <= number of words <= 1000
- 1 <= len(word) <= 100
- Words contain only lowercase English letters

EXAMPLES
--------
Input:
  banana apple kiwi cherry fig
Output: fig kiwi apple banana cherry

Input:
  cat bat ant
Output: ant bat cat

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(words: list[str]) -> list[str]:
    """Sort strings by length ascending, then alphabetically for ties."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = input().split()
    print(*solve(data))
