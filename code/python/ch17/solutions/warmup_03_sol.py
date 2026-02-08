"""
Solution for Warmup 3: Last Stone Weight
============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a max-heap (negate values). Each turn, pop two largest stones.
If they differ, push the difference back. Continue until <= 1 stone remains.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""

import heapq


def solve(stones: list[int]) -> int:
    """Return the weight of the last remaining stone, or 0."""
    # Negate for max-heap behavior
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)   # Largest
        second = -heapq.heappop(heap)  # Second largest
        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    stones = list(map(int, input().strip().split()))
    print(solve(stones))
