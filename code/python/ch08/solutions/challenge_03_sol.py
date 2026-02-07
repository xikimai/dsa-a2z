"""
Solution for Challenge 3: Sort by Frequency
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Build a frequency map using collections.Counter. Sort with a custom key:
  - Primary: -freq[x] (descending frequency — negate so higher freq comes first)
  - Secondary: x (ascending value for tiebreaker)

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""

from collections import Counter


def solve(arr: list[int]) -> list[int]:
    """Sort by frequency descending, tiebreak by value ascending."""
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
