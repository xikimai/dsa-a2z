"""
Solution for Challenge 4: Kth Element of Two Sorted Arrays
===========================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on how many elements to take from the first array.
If we take i from nums1, we take k-i from nums2. Check partition validity.

TIME COMPLEXITY:  O(log(min(m, n, k)))
SPACE COMPLEXITY: O(1)
"""


def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    """Return the kth smallest element (1-indexed) from two sorted arrays."""
    pass  # TODO: Replace this with your solution

    # Ensure nums1 is the shorter array
    if m > n:
        return solve(nums2, nums1, k)

    # lo = min elements we must take from nums1
    # hi = max elements we can take from nums1
    lo = max(0, k - n)
    hi = min(k, m)

    while lo <= hi:
        i = lo + (hi - lo) // 2  # take i elements from nums1
        j = k - i                 # take j elements from nums2

        left1 = nums1[i - 1] if i > 0 else float("-inf")
        left2 = nums2[j - 1] if j > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")
        right2 = nums2[j] if j < n else float("inf")

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        elif left1 > right2:
            hi = i - 1
        else:
            lo = i + 1

    return -1  # should not reach here


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    k = int(input().strip())
    nums1 = list(map(int, line1.split())) if line1 else []
    nums2 = list(map(int, line2.split())) if line2 else []
    print(solve(nums1, nums2, k))
