"""
Solution for Practice 2: Merge K Sorted Arrays
==================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a min-heap of (value, array_index, element_index). Pop the minimum,
append to result, and push the next element from the same array.

TIME COMPLEXITY:  O(N log K) where N = total elements, K = number of arrays
SPACE COMPLEXITY: O(K) for the heap + O(N) for the result
"""

import heapq


def solve(arrays: list[list[int]]) -> list[int]:
    """Merge K sorted arrays into one sorted array."""
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    arrays = json.loads(input().strip())
    print(solve(arrays))
