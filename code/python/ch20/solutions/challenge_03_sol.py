"""
Solution for Challenge 3: Making a Large Island
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
1. Label each island with a unique ID using BFS, recording size of each.
2. For each 0-cell, look at its 4 neighbors' island IDs (use a set to
   avoid double-counting). The potential island = 1 + sum of unique
   neighbor island sizes.
3. Return the maximum.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n^2)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return largest island size after flipping at most one 0."""
    n = len(grid)
    if n == 0:
        return 0

    island_id = [[0] * n for _ in range(n)]
    island_size = {}  # id -> size
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    current_id = 2  # Start from 2 to avoid confusion with 0 and 1

    # Step 1: Label all islands
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1 and island_id[r][c] == 0:
                # BFS to label this island
                queue = deque([(r, c)])
                island_id[r][c] = current_id
                size = 0
                while queue:
                    cr, cc = queue.popleft()
                    size += 1
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        if (0 <= nr < n and 0 <= nc < n
                                and grid[nr][nc] == 1 and island_id[nr][nc] == 0):
                            island_id[nr][nc] = current_id
                            queue.append((nr, nc))
                island_size[current_id] = size
                current_id += 1

    # If no islands, flipping one 0 gives size 1
    if not island_size:
        return 1

    # If entire grid is land, no 0 to flip
    max_size = max(island_size.values())

    # Step 2: Check each 0-cell
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbor_ids = set()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and island_id[nr][nc] != 0:
                        neighbor_ids.add(island_id[nr][nc])
                total = 1 + sum(island_size[iid] for iid in neighbor_ids)
                max_size = max(max_size, total)

    return max_size


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
