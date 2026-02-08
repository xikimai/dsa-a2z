"""
Solution for Practice 3: Longest Subarray with Sum K
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Use prefix sums with a hash map. Store the earliest index where each
prefix sum occurs. For each position j, if prefix_sum[j] - k exists
in the map at index i, then the subarray from i+1 to j has sum k.
Track the maximum length.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the prefix sum map
"""


def solve(arr: list[int], k: int) -> int:
    """Return length of longest contiguous subarray with sum K."""
    prefix_map = {0: -1}  # prefix_sum -> earliest index
    prefix_sum = 0
    max_len = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_len = max(max_len, length)

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
