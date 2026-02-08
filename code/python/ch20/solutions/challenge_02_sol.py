"""
Solution for Challenge 2: Shortest Bridge
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
1. Find the first island via BFS, collecting all its cells.
2. Multi-source BFS from that island outward through water.
3. When BFS reaches a cell of value 1 (the other island), return the distance.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n^2)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum flips to connect two islands."""
    n = len(grid)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # Step 1: Find first island via BFS
    queue = deque()
    found = False
    for r in range(n):
        if found:
            break
        for c in range(n):
            if grid[r][c] == 1:
                # BFS to collect entire first island
                bfs = deque([(r, c)])
                grid[r][c] = 2  # mark as island 1
                while bfs:
                    cr, cc = bfs.popleft()
                    queue.append((cr, cc, 0))  # add to multi-source BFS
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            bfs.append((nr, nc))
                found = True
                break

    # Step 2: Multi-source BFS from island 1 to find island 2
    while queue:
        r, c, dist = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    return dist
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 2  # mark visited
                    queue.append((nr, nc, dist + 1))

    return -1  # Should never reach here with valid input


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
