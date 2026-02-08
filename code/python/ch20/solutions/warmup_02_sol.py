"""
Solution for Warmup 2: Number of Islands
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
Scan grid. For each unvisited 1, BFS flood fill and increment counter.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return the number of islands in the grid."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = 0
                while queue:
                    cr, cc = queue.popleft()
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
