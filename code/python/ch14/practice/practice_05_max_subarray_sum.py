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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

