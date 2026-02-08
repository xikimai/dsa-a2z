"""
Solution for Challenge 3: Median of Two Sorted Arrays
======================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on the partition point of the shorter array. Partition both
arrays so left halves contain exactly half the total elements. Check that
max(left) <= min(right) to find the correct partition.

TIME COMPLEXITY:  O(log(min(m, n)))
SPACE COMPLEXITY: O(1)
"""


def solve(nums1: list[int], nums2: list[int]) -> float:
    """Return the median of two sorted arrays."""
    # Ensure nums1 is the shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2

    lo, hi = 0, m
    while lo <= hi:
        i = lo + (hi - lo) // 2  # partition in nums1
        j = half - i              # partition in nums2

        # Edge values
        left1 = nums1[i - 1] if i > 0 else float("-inf")
        left2 = nums2[j - 1] if j > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")
        right2 = nums2[j] if j < n else float("inf")

        if left1 <= right2 and left2 <= right1:
            # Correct partition found
            if (m + n) % 2 == 1:
                return float(max(left1, left2))
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            hi = i - 1  # too many from nums1
        else:
            lo = i + 1  # too few from nums1

    return 0.0  # should not reach here


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    nums1 = list(map(int, line1.split())) if line1 else []
    nums2 = list(map(int, line2.split())) if line2 else []
    print(solve(nums1, nums2))
