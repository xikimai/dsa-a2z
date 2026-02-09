"""
Solution for Warmup 4: Shortest Path in Binary Matrix
======================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
BFS from (0,0) to (n-1,n-1) with 8-directional moves. Each step costs 1.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n^2)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return shortest path length in binary matrix, or -1."""
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    if n == 1:
        return 1

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
    q = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0] = 1  # mark visited

    while q:
        r, c, length = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                if nr == n - 1 and nc == n - 1:
                    return length + 1
                grid[nr][nc] = 1
                q.append((nr, nc, length + 1))

    return -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
