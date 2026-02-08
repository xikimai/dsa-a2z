"""
Solution for Challenge 3: Subarray Sum Divisible by K
======================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Use prefix sums modulo k. Two prefix sums with the same remainder
mean the subarray between them has sum divisible by k.
Count remainders and use c*(c-1)/2 formula for pairs.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(min(n, k)) — remainder counts
"""


def solve(arr: list[int], k: int) -> int:
    """Return count of subarrays with sum divisible by k."""
    remainder_count = {0: 1}
    current_sum = 0
    count = 0

    for x in arr:
        current_sum += x
        rem = current_sum % k  # Python handles negative mod correctly
        count += remainder_count.get(rem, 0)
        remainder_count[rem] = remainder_count.get(rem, 0) + 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
