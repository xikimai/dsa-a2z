"""
Solution for Practice 5: K Closest Points to Origin
=======================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a max-heap of size k (negate distances). For each point, push
its negated squared distance. If heap exceeds size k, pop the farthest.
Final result sorted by distance.

TIME COMPLEXITY:  O(n log k)
SPACE COMPLEXITY: O(k)
"""

import heapq


def solve(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the k closest points to origin, sorted by distance."""
    # Max-heap of size k: (-dist_sq, x, y)
    heap = []
    for x, y in points:
        dist_sq = x * x + y * y
        heapq.heappush(heap, (-dist_sq, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    # Extract and sort by distance
    result = [[x, y] for neg_dist, x, y in heap]
    result.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    points = json.loads(input().strip())
    k = int(input().strip())
    print(solve(points, k))
