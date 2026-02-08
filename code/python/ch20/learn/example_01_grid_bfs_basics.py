"""
Example 1: Grid BFS Basics
==============================
Chapter 20: Graphs II — Real Problems

Demonstrates:
- Treating a 2D grid as a graph
- 4-directional BFS with direction arrays
- Flood fill (paint bucket algorithm)
- Counting connected components (islands)
"""

from collections import deque


# ── Helper: print a grid nicely ──────────────────────────────────────
def print_grid(grid, label=""):
    if label:
        print(f"\n{label}:")
    for row in grid:
        print("  ", " ".join(str(x) for x in row))


# ── 1. Grid BFS: visit all reachable cells from a start ─────────────
def grid_bfs(grid, start_r, start_c):
    """BFS from (start_r, start_c), returning list of visited cells in order."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    order = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        order.append((r, c))
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return order


# ── 2. Flood Fill ────────────────────────────────────────────────────
def flood_fill(image, sr, sc, new_color):
    """Change the color of all cells connected to (sr, sc) with the same color."""
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]
    if original == new_color:
        return image  # Avoid infinite loop!

    queue = deque([(sr, sc)])
    image[sr][sc] = new_color
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image


# ── 3. Count Islands (connected components) ──────────────────────────
def count_islands(grid):
    """Count the number of connected components of 1's in the grid."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                # BFS to mark entire island
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    cr, cc = queue.popleft()
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        if (0 <= nr < rows and 0 <= nc < cols
                                and not visited[nr][nc] and grid[nr][nc] == 1):
                            visited[nr][nc] = True
                            queue.append((nr, nc))

    return count


# ── Demo ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Demo 1: Grid BFS
    print("=" * 50)
    print("DEMO 1: Grid BFS Traversal")
    print("=" * 50)
    grid1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 1, 0],
    ]
    print_grid(grid1, "Grid (1=land, 0=water)")
    order = grid_bfs(grid1, 0, 0)
    print(f"  BFS from (0,0) visits: {order}")

    # Demo 2: Flood Fill
    print("\n" + "=" * 50)
    print("DEMO 2: Flood Fill (Paint Bucket)")
    print("=" * 50)
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    print_grid(image, "Before (painting from (1,1) with color 2)")
    flood_fill(image, 1, 1, 2)
    print_grid(image, "After")

    # Demo 3: Count Islands
    print("\n" + "=" * 50)
    print("DEMO 3: Count Islands")
    print("=" * 50)
    grid2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    print_grid(grid2, "Grid")
    print(f"  Number of islands: {count_islands(grid2)}")
    # Expected: 3 islands
