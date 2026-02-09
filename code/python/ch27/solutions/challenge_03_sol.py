"""
Solution for Challenge 3: Minimum Cost to Make Valid Path
==========================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
0-1 BFS. From each cell, try all 4 directions. If direction matches
the arrow, cost = 0. Otherwise, cost = 1.
Arrow encoding: 1=right, 2=left, 3=down, 4=up.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum cost to create a valid path from (0,0) to (m-1,n-1)."""
    m, n = len(grid), len(grid[0])
    # direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    dir_map = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    arrow_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # same order as 1,2,3,4

    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 0
    dq = deque([(0, 0)])

    while dq:
        r, c = dq.popleft()
        arrow_dr, arrow_dc = dir_map[grid[r][c]]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = 0 if (dr == arrow_dr and dc == arrow_dc) else 1
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
