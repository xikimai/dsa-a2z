"""
Solution for Warmup 2: Sort Using Heap (Heapsort)
=====================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use heapq.heapify to build a min-heap in O(n), then pop all elements.
Each pop is O(log n), so total is O(n log n).

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n) for the result array
"""

import heapq


def solve(arr: list[int]) -> list[int]:
    """Return arr sorted in ascending order using a heap."""
    heap = arr[:]
    heapq.heapify(heap)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
