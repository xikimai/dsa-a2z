"""
Solution for Practice 5: Number of Enclaves
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
BFS from all border land cells to mark them as visited. Count remaining
unvisited land cells.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return count of land cells that cannot reach the boundary."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # Enqueue all border land cells
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                queue.append((r, c))
                grid[r][c] = 0  # mark visited

    # BFS to mark all land connected to border
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))

    # Count remaining land
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
