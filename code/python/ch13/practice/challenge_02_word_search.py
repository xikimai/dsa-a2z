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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    for _ in range(m):
        board.append(input().split())
    word = input().strip()
    print(solve(board, word))

