"""
Solution for Challenge 2: Maximum Subarray Sum Three Ways
==========================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Three methods with decreasing time complexity.

TIME/SPACE:
  solve_brute:  O(n^3) / O(1)
  solve_prefix: O(n^2) / O(n)
  solve_kadane: O(n)   / O(1)
"""


def solve_brute(arr: list[int]) -> int:
    """O(n^3) brute force: try every subarray, sum each one."""
    if not arr:
        return 0
    n = len(arr)
    max_sum = arr[0]
    for l in range(n):
        for r in range(l, n):
            total = 0
            for k in range(l, r + 1):
                total += arr[k]
            max_sum = max(max_sum, total)
    return max_sum


def solve_prefix(arr: list[int]) -> int:
    """O(n^2) prefix sum: precompute prefix, try all (l, r) pairs."""
    if not arr:
        return 0
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    max_sum = arr[0]
    for l in range(n):
        for r in range(l, n):
            total = prefix[r + 1] - prefix[l]
            max_sum = max(max_sum, total)
    return max_sum


def solve_kadane(arr: list[int]) -> int:
    """O(n) Kadane's: extend-or-restart in one pass."""
    if not arr:
        return 0
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    b = solve_brute(arr)
    p = solve_prefix(arr)
    k = solve_kadane(arr)
    print(f"brute={b} prefix={p} kadane={k}")
