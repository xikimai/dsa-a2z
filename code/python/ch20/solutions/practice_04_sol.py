"""
Solution for Practice 4: Shortest Path in Binary Matrix
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
BFS from (0,0) with 8-directional movement. Return path length when
reaching (n-1, n-1). Path length = number of cells visited.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n^2)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return length of shortest path, or -1 if impossible."""
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    if n == 1:
        return 1

    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0] = 1  # mark visited

    # 8-directional
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                if nr == n - 1 and nc == n - 1:
                    return dist + 1
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
