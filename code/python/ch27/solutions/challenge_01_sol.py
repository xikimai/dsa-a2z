"""
Solution for Challenge 1: Minimum Obstacle Removal to Reach Corner
===================================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
0-1 BFS. Empty cell (0) costs 0, obstacle (1) costs 1 to remove.
Push 0-cost moves to front of deque, 1-cost to back.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum obstacles to remove."""
    m, n = len(grid), len(grid[0])
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 0
    dq = deque([(0, 0)])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while dq:
        r, c = dq.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = grid[nr][nc]  # 0 or 1
                if dist[r][c] + cost < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + cost
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    return dist[m - 1][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
