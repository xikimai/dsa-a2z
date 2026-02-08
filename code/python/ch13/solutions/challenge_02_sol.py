"""
Solution for Challenge 2: Word Search
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Try starting from each cell. Backtrack: check if current cell matches
current character, mark visited, try all 4 directions, un-mark.

TIME COMPLEXITY:  O(m * n * 4^L) — L = word length
SPACE COMPLEXITY: O(L) — recursion depth
"""


def solve(board: list[list[str]], word: str) -> bool:
    """Return True if word exists in the grid."""
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        # Mark as visited
        temp = board[r][c]
        board[r][c] = '#'

        # Try all 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if backtrack(r + dr, c + dc, index + 1):
                board[r][c] = temp  # Restore before returning
                return True

        # Un-mark (backtrack)
        board[r][c] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    for _ in range(m):
        board.append(input().split())
    word = input().strip()
    print(solve(board, word))
