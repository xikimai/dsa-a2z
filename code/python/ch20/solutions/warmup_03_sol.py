"""
Solution for Warmup 3: Max Area of Island
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
BFS flood fill for each unvisited 1, counting cells per component.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return the maximum area of an island."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = 0
                queue = deque([(r, c)])
                grid[r][c] = 0
                while queue:
                    cr, cc = queue.popleft()
                    area += 1
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))
                max_area = max(max_area, area)

    return max_area


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
