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
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    total = prefix[n]
    for i in range(n):
        left_sum = prefix[i]
        right_sum = total - prefix[i + 1]
        if left_sum == right_sum:
            return i
    return -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
