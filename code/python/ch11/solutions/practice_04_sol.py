"""
Solution for Practice 4: Count Subarrays with Sum K
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Use prefix sums with a frequency hash map. Initialize with {0: 1}.
For each prefix sum, add the count of (prefix_sum - k) from the map,
then increment the count of the current prefix sum.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the prefix sum frequency map
"""


def solve(arr: list[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals K."""
    prefix_freq = {0: 1}
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        need = prefix_sum - k
        count += prefix_freq.get(need, 0)
        prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
