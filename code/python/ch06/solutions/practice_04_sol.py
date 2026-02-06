"""
Solution for Practice 4: Majority Element
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Boyer-Moore Voting Algorithm:
  1. Keep a candidate and a count (both start at 0).
  2. For each element:
     - If count is 0, adopt the current element as candidate.
     - If current == candidate, count += 1.
     - Otherwise, count -= 1.
  3. The surviving candidate is the majority element.

Why it works: every "cancellation" (count -= 1) pairs one non-majority
element with one majority element.  Since the majority appears > n/2
times, it always survives.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the majority element using Boyer-Moore Voting."""
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
