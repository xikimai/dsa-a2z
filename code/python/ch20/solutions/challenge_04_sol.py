"""
Solution for Challenge 4: Swim in Rising Water
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
Binary search on time t. For each candidate t, BFS/DFS to check if
(0,0) can reach (n-1,n-1) using only cells with elevation <= t.

TIME COMPLEXITY:  O(n^2 * log(n^2))
SPACE COMPLEXITY: O(n^2)
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum time to swim from (0,0) to (n-1,n-1)."""
    n = len(grid)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def can_reach(t):
        """Check if we can reach (n-1,n-1) from (0,0) at time t."""
        if grid[0][0] > t:
            return False
        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return True
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if (0 <= nr < n and 0 <= nc < n
                        and not visited[nr][nc] and grid[nr][nc] <= t):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return False

    lo = max(grid[0][0], grid[n - 1][n - 1])
    hi = n * n - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if can_reach(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
