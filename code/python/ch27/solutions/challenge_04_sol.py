"""
Solution for Challenge 4: Path with Maximum Minimum Value
==========================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Modified Dijkstra using a MAX-heap. We want to maximize the minimum value
on the path. dist[r][c] = best (largest) minimum value to reach (r,c).
Relax: new_val = min(dist[r][c], grid[nr][nc]). Take max with dist[nr][nc].
Use negative values with heapq to simulate max-heap.

TIME COMPLEXITY:  O(m * n * log(m * n))
SPACE COMPLEXITY: O(m * n)
"""

import heapq


def solve(grid: list[list[int]]) -> int:
    """Return the maximum minimum value on any path from (0,0) to (m-1,n-1)."""
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    # Max-heap via negative values
    heap = [(-grid[0][0], 0, 0)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        neg_d, r, c = heapq.heappop(heap)
        d = -neg_d
        if d < dist[r][c]:
            continue
        if r == m - 1 and c == n - 1:
            return d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_val = min(d, grid[nr][nc])
                if new_val > dist[nr][nc]:
                    dist[nr][nc] = new_val
                    heapq.heappush(heap, (-new_val, nr, nc))

    return dist[m - 1][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
