"""
Solution for Practice 1: Rotten Oranges
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
Multi-source BFS from all initially rotten oranges. Track fresh count.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minutes until all oranges are rotten, or -1 if impossible."""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes if fresh == 0 else -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
