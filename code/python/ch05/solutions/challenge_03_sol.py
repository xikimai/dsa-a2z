"""
Solution for Challenge 3: Rotate Array
========================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
The three-reverse trick:
1. Normalize k: k = k % n (handles k > length).
2. Reverse the entire list.
3. Reverse the first k elements.
4. Reverse the remaining n - k elements.

Why it works: rotating right by k means the last k elements move to
the front. Reversing the whole list puts them at the front (but in
reverse order). Then we reverse each half to restore the correct order.

Example: [1,2,3,4,5,6,7], k=3
  Step 1: [7,6,5,4,3,2,1]  (reverse all)
  Step 2: [5,6,7,4,3,2,1]  (reverse first 3)
  Step 3: [5,6,7,1,2,3,4]  (reverse last 4)

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) — done in place
"""


def solve(nums: list[int], k: int) -> list[int]:
    """Rotate the list to the right by k steps and return it."""
    n = len(nums)
    if n == 0:
        return nums

    k = k % n
    if k == 0:
        return nums

    def reverse(lst, start, end):
        """Reverse elements in lst from index start to end (inclusive)."""
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    return nums


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    result = solve(nums, k)
    print(" ".join(map(str, result)))
