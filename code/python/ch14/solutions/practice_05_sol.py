"""
Solution for Practice 5: Maximum Subarray Sum (Kadane's Algorithm)
===================================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Kadane's algorithm: maintain current_sum and max_sum.
At each position, extend or restart.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> int:
    """Return the maximum subarray sum."""
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
    print(solve(arr))
