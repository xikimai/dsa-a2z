"""
Solution for Practice 4: Find Median from Data Stream
=========================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use two heaps:
  - max_heap (lower half): stores negated values for max-heap behavior
  - min_heap (upper half): standard min-heap
Balance: max_heap can have at most 1 more element than min_heap.

TIME COMPLEXITY:  O(n log n) total — O(log n) per add_num
SPACE COMPLEXITY: O(n)
"""

import heapq


def solve(nums: list[int]) -> list[float]:
    """Return a list of medians after adding each number."""
    max_heap = []  # Lower half (negated for max-heap)
    min_heap = []  # Upper half
    medians = []

    for num in nums:
        # Add to max_heap (lower half) first
        heapq.heappush(max_heap, -num)

        # Ensure max of lower half <= min of upper half
        if min_heap and -max_heap[0] > min_heap[0]:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)

        # Balance sizes: max_heap can have at most 1 more element
        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)

        # Calculate median
        if len(max_heap) > len(min_heap):
            medians.append(float(-max_heap[0]))
        else:
            medians.append((-max_heap[0] + min_heap[0]) / 2.0)

    return medians


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
