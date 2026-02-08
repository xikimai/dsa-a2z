"""
Solution for Challenge 3: Sliding Window Maximum
====================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a monotone decreasing deque. For each element:
1. Remove elements from the back that are smaller (they can never be the max).
2. Add the current element's index.
3. Remove the front if it's outside the window.
4. The front of the deque is always the max for the current window.

TIME COMPLEXITY:  O(n) — each element enters and leaves the deque once
SPACE COMPLEXITY: O(k) for the deque
"""

from collections import deque


def solve(nums: list[int], k: int) -> list[int]:
    """Return the maximum in each sliding window of size k."""
    dq = deque()  # Stores indices, monotone decreasing by value
    result = []

    for i in range(len(nums)):
        # Remove elements smaller than current from the back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Remove front if outside window
        if dq[0] <= i - k:
            dq.popleft()

        # Window is fully formed when i >= k - 1
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
