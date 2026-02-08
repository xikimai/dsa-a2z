"""
Solution for Practice 1: Top K Frequent Elements
====================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
1. Build a frequency map.
2. Use a min-heap of size k keyed by frequency.
3. Return the k elements with highest frequency, sorted.

TIME COMPLEXITY:  O(n + m log k) where m = unique elements
SPACE COMPLEXITY: O(n) for the frequency map
"""

import heapq
from collections import Counter


def solve(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements, sorted ascending."""
    freq = Counter(nums)
    # Min-heap of (frequency, value) — keeps top k by frequency
    heap = []
    for val, cnt in freq.items():
        heapq.heappush(heap, (cnt, val))
        if len(heap) > k:
            heapq.heappop(heap)
    result = sorted(val for cnt, val in heap)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
