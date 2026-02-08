"""
Solution for Challenge 1: Walls and Gates
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
Multi-source BFS from all gates (cells with value 0). Each BFS level
increments distance by 1. Walls (-1) block traversal.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque

INF = 2147483647


def solve(rooms: list[list[int]]) -> list[list[int]]:
    """Fill each empty room with distance to nearest gate."""
    if not rooms or not rooms[0]:
        return rooms

    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # Enqueue all gates
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    # BFS
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

    return rooms


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    rooms = []
    for _ in range(rows):
        rooms.append(list(map(int, input().split())))
    solve(rooms)
    for row in rooms:
        print(" ".join(map(str, row)))
