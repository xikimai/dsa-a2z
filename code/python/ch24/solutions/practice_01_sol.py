"""
Solution for Practice 1: Unique Paths III
==========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Backtracking/DFS. Count empty cells (including start). DFS from start,
marking cells visited. When reaching end, check if all cells visited.

TIME COMPLEXITY:  O(3^(m*n)) worst case (backtracking)
SPACE COMPLEXITY: O(m*n) for the recursion stack
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the number of paths visiting every non-obstacle cell exactly once."""
    m, n = len(grid), len(grid[0])
    start_r = start_c = 0
    empty = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                start_r, start_c = i, j
                empty += 1  # start cell counts as a cell to visit
            elif grid[i][j] == 0:
                empty += 1

    result = 0

    def dfs(r, c, remaining):
        nonlocal result
        if grid[r][c] == 2:
            if remaining == 0:
                result += 1
            return
        temp = grid[r][c]
        grid[r][c] = -2  # mark visited
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1 and grid[nr][nc] != -2:
                dfs(nr, nc, remaining - 1)
        grid[r][c] = temp  # restore

    dfs(start_r, start_c, empty)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
