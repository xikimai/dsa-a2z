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
    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for x in arr:
        current_sum += x
        complement = current_sum - k
        count += prefix_count.get(complement, 0)
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
