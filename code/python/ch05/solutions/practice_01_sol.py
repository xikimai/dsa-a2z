"""
Solution for Practice 1: Union of Two Arrays
==============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Add all elements from both lists into a set (which automatically removes
duplicates), then convert to a sorted list.

TIME COMPLEXITY:  O((n + m) * log(n + m)) — dominated by sorting
SPACE COMPLEXITY: O(n + m) for the set
"""


def solve(a: list[int], b: list[int]) -> list[int]:
    """Return the sorted union of two lists (unique elements from both)."""
    return sorted(set(a) | set(b))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(a, b)
    print(" ".join(map(str, result)))
