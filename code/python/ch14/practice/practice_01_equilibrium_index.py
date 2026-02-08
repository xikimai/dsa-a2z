"""
Solution for Practice 1: Equilibrium Index
============================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Build prefix sum. For each index i, left_sum = prefix[i],
right_sum = prefix[n] - prefix[i+1]. Return first i where they match.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — prefix array
"""


def solve(arr: list[int]) -> int:
    """Return the first equilibrium index, or -1 if none."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

