"""
Challenge 4: Kth Element of Two Sorted Arrays
===============================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given two sorted arrays and an integer k (1-indexed), find the kth
smallest element in the combined sorted order.

INPUT FORMAT
------------
First line: space-separated integers (first sorted array, may be empty).
Second line: space-separated integers (second sorted array, may be empty).
Third line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the kth smallest element.

CONSTRAINTS
-----------
- 0 <= len(nums1), len(nums2) <= 10^5
- 1 <= k <= len(nums1) + len(nums2)
- -10^6 <= nums1[i], nums2[i] <= 10^6
- Both arrays are sorted

EXAMPLES
--------
Input:
  2 3 6 7 9
  1 4 8 10
  5
Output: 6

Input:
  1 3 5
  2 4 6
  1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
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
