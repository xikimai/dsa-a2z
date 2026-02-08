"""
Solution for Warmup 3: Max Sum of Fixed Window
================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Build the first window sum, then slide by subtracting the leaving
element and adding the entering element. Track the maximum.

TIME COMPLEXITY:  O(n) — single pass after initial window
SPACE COMPLEXITY: O(1) — constant extra space
"""


def solve(arr: list[int], k: int) -> int:
    """Return maximum sum of k consecutive elements."""
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    best = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)

    return best


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    k = int(input().strip())
    print(solve(arr, k))
