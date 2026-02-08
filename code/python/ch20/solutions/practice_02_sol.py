"""
Solution for Practice 2: 01 Matrix
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
Multi-source BFS from all 0-cells. Each level increments distance by 1.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(mat: list[list[int]]) -> list[list[int]]:
    """Return distance of each cell to nearest 0."""
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


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    mat = []
    for _ in range(rows):
        mat.append(list(map(int, input().split())))
    result = solve(mat)
    for row in result:
        print(" ".join(map(str, row)))
