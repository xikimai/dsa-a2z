"""
Solution for Practice 3: Rat in a Maze
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Backtrack from (0,0). Try directions D, L, R, U in alphabetical order
so paths come out sorted. Mark visited to avoid cycles.

TIME COMPLEXITY:  O(4^(n^2)) worst case — exponential
SPACE COMPLEXITY: O(n^2) — visited grid + recursion depth
"""


def solve(maze: list[list[int]]) -> list[str]:
    """Return all paths from (0,0) to (N-1,N-1), sorted."""
    n = len(maze)
    if n == 0 or maze[0][0] == 0:
        return []

    results = []
    visited = [[False] * n for _ in range(n)]
    # Directions in alphabetical order: D, L, R, U
    directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

    def backtrack(r, c, path):
        if r == n - 1 and c == n - 1:
            results.append(path)
            return

        for d_name, dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                backtrack(nr, nc, path + d_name)
                visited[nr][nc] = False

    visited[0][0] = True
    backtrack(0, 0, "")
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    result = solve(maze)
    for path in result:
        print(path)
