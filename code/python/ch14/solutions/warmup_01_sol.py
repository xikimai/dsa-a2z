"""
Solution for Warmup 1: Build Prefix Sum Array
===============================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Build the prefix array iteratively using prefix[i] = prefix[i-1] + arr[i-1].

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — the prefix array
"""


def solve(arr: list[int]) -> list[int]:
    """Return the prefix sum array of length n+1."""
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
