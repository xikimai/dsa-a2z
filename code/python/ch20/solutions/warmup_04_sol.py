"""
Solution for Warmup 4: Surrounded Regions
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
1. BFS from all border 'O's, marking them as 'S' (safe).
2. Flip remaining 'O's to 'X', then flip 'S' back to 'O'.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(board: list[list[str]]) -> list[list[str]]:
    """Capture surrounded regions in-place and return the board."""
    if not board or not board[0]:
        return board

    rows, cols = len(board), len(board[0])
    queue = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # Enqueue border O's
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                queue.append((r, c))
                board[r][c] = 'S'

    # BFS to mark all O's connected to border
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                board[nr][nc] = 'S'
                queue.append((nr, nc))

    # Flip remaining O's to X, S back to O
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'

    return board


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    board = []
    for _ in range(rows):
        board.append(input().split())
    solve(board)
    for row in board:
        print(" ".join(row))
