"""
Example 2: Multi-Source BFS
==============================
Chapter 20: Graphs II — Real Problems

Demonstrates:
- Multi-source BFS (rotten oranges concept)
- Distance to nearest source (01 matrix)
- 0-1 BFS with a deque
"""

from collections import deque


def print_grid(grid, label=""):
    if label:
        print(f"\n{label}:")
    for row in grid:
        print("  ", " ".join(f"{x:2d}" for x in row))


# ── 1. Rotten Oranges (Multi-Source BFS) ─────────────────────────────
def rotten_oranges(grid):
    """
    0 = empty, 1 = fresh, 2 = rotten.
    Each minute, rotten oranges rot adjacent fresh ones.
    Return minutes to rot all, or -1 if impossible.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Enqueue ALL rotten oranges
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


# ── 2. Distance to Nearest Zero (Multi-Source BFS) ───────────────────
def nearest_zero_distance(mat):
    """Return distance of each cell to nearest 0 using multi-source BFS."""
    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


# ── 3. 0-1 BFS Demo ─────────────────────────────────────────────────
def zero_one_bfs(grid):
    """
    Shortest path from (0,0) to (rows-1, cols-1).
    grid[r][c] = 0 means free move, 1 means cost-1 move.
    Uses deque: cost-0 to front, cost-1 to back.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    dq = deque([(0, 0)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while dq:
        r, c = dq.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols:
                w = grid[nr][nc]
                if dist[r][c] + w < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + w
                    if w == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    return dist[rows - 1][cols - 1]


# ── Demo ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Demo 1: Rotten Oranges
    print("=" * 50)
    print("DEMO 1: Rotten Oranges")
    print("=" * 50)
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print_grid(grid1, "Grid (0=empty, 1=fresh, 2=rotten)")
    result = rotten_oranges(grid1)
    print(f"  Minutes to rot all: {result}")  # Expected: 4

    # Demo 2: Distance to Nearest Zero
    print("\n" + "=" * 50)
    print("DEMO 2: Distance to Nearest Zero")
    print("=" * 50)
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    print_grid(mat, "Input matrix")
    distances = nearest_zero_distance(mat)
    print_grid(distances, "Distances to nearest 0")
    # Expected:
    # 0 0 0
    # 0 1 0
    # 1 2 1

    # Demo 3: 0-1 BFS
    print("\n" + "=" * 50)
    print("DEMO 3: 0-1 BFS (cheapest path)")
    print("=" * 50)
    grid2 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
    print_grid(grid2, "Grid (0=free, 1=cost)")
    result = zero_one_bfs(grid2)
    print(f"  Cheapest path cost from (0,0) to (2,2): {result}")  # Expected: 0
