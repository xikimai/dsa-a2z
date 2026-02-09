"""
Solution for Challenge 2: Making a Large Island
=================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
1. Label each connected component of 1s with Union-Find, track component sizes.
2. For each 0 cell, check the 4 adjacent cells and sum up the sizes of
   distinct neighboring components + 1 (for the flipped cell).
3. Return the maximum.

TIME COMPLEXITY:  O(n^2 * alpha(n^2))
SPACE COMPLEXITY: O(n^2)
"""


def solve(grid: list[list[int]]) -> int:
    """Return the largest island size after flipping at most one 0 to 1."""
    n = len(grid)
    parent = list(range(n * n))
    rank = [0] * (n * n)
    size = [1] * (n * n)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
            size[ry] += size[rx]
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
            size[rx] += size[ry]
        else:
            parent[ry] = rx
            size[rx] += size[ry]
            rank[rx] += 1

    def idx(r, c):
        return r * n + c

    # Step 1: Union all adjacent 1s
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        union(idx(r, c), idx(nr, nc))

    # Step 2: For each 0, try flipping and compute merged size
    best = 0
    # First check max existing component
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                best = max(best, size[find(idx(r, c))])

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen = set()
                total = 1  # the flipped cell
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        root = find(idx(nr, nc))
                        if root not in seen:
                            seen.add(root)
                            total += size[root]
                best = max(best, total)

    return best


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        grid.append(row)
    print(solve(grid))
