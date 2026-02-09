"""
Solution for Practice 5: Swim in Rising Water
===============================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Dijkstra where "distance" = max elevation on the path so far.
Relax: new_dist = max(dist[r][c], grid[nr][nc]).

TIME COMPLEXITY:  O(n^2 * log(n^2))
SPACE COMPLEXITY: O(n^2)
"""

import heapq


def solve(grid: list[list[int]]) -> int:
    """Return minimum time to swim from (0,0) to (n-1,n-1)."""
    n = len(grid)
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r][c]:
            continue
        if r == n - 1 and c == n - 1:
            return d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                new_d = max(d, grid[nr][nc])
                if new_d < dist[nr][nc]:
                    dist[nr][nc] = new_d
                    heapq.heappush(heap, (new_d, nr, nc))

    return dist[n - 1][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
