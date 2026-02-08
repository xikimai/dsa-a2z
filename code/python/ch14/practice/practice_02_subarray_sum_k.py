"""
Solution for Practice 2: Subarray Sum Equals K (Count)
=======================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Prefix sum + hash map. Maintain running sum and a map of
{prefix_sum: count}. For each position, check how many
previous prefix sums equal current_sum - k.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — hash map
"""


def solve(arr: list[int], k: int) -> int:
    """Return count of subarrays with sum equal to k."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))

