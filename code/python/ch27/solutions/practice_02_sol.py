"""
Solution for Practice 2: Path with Minimum Effort
===================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Dijkstra on grid. dist[r][c] = minimum effort to reach (r,c).
Edge weight = abs(heights[r][c] - heights[nr][nc]).
Relax: new_effort = max(dist[r][c], abs_diff). Take min with dist[nr][nc].

TIME COMPLEXITY:  O(m * n * log(m * n))
SPACE COMPLEXITY: O(m * n)
"""

import heapq


def solve(heights: list[list[int]]) -> int:
    """Return the minimum effort path value."""
    m, n = len(heights), len(heights[0])
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (effort, row, col)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        effort, r, c = heapq.heappop(heap)
        if effort > dist[r][c]:
            continue
        if r == m - 1 and c == n - 1:
            return effort
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                if new_effort < dist[nr][nc]:
                    dist[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

    return dist[m - 1][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    heights = json.loads(sys.stdin.read().strip())
    print(solve(heights))
