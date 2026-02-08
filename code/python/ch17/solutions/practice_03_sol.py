"""
Solution for Practice 3: Kth Smallest Element in a Sorted Matrix
====================================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a min-heap. Push the first element of each row (value, row, col).
Pop k-1 times, each time pushing the next element from the same row.
The kth pop is the answer.

TIME COMPLEXITY:  O(k log n) where n = number of rows
SPACE COMPLEXITY: O(n) for the heap
"""

import heapq


def solve(matrix: list[list[int]], k: int) -> int:
    """Return the kth smallest element in the sorted matrix."""
    n = len(matrix)
    # Push first element of each row
    heap = []
    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    # Pop k times
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return val


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    data = json.loads(input().strip())
    k = int(input().strip())
    print(solve(data, k))
