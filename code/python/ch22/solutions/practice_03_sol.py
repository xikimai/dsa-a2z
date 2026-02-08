"""
Solution for Practice 3: Sliding Window Maximum
====================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a deque storing indices in decreasing order of values.
For each new element: remove expired indices from front,
remove smaller elements from back, add new index.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(k)
"""

from collections import deque


def solve(nums: list[int], k: int) -> list[int]:
    """Return the maximum in each sliding window of size k."""
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove expired indices
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        # Window fully formed
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
