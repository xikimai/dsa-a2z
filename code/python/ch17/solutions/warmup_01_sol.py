"""
Solution for Warmup 1: Kth Largest Element
=============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a min-heap of size k. For each element, push it. If heap size
exceeds k, pop the smallest. At the end, the heap root is the kth largest.

TIME COMPLEXITY:  O(n log k)
SPACE COMPLEXITY: O(k)
"""

import heapq


def solve(nums: list[int], k: int) -> int:
    """Return the kth largest element in nums."""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
