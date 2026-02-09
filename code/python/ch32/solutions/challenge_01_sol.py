"""
Solution for Challenge 1: Word Search II (Trie + Backtracking)
===============================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
1. Build a Trie from the word list.
2. For each cell on the board, start a DFS/backtracking search.
3. At each step, check if the current path exists in the Trie.
   If not, prune (stop exploring that direction).
4. If we reach a word-end node, add the word to results.
5. To avoid duplicates, remove the word from the Trie after finding it.

TIME COMPLEXITY:  O(rows * cols * 4^L) where L = max word length, but
                  Trie pruning makes it much faster in practice.
SPACE COMPLEXITY: O(sum of word lengths) for the Trie
"""


def solve(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all words from the list that can be formed by adjacent cells on the board."""
    if not board or not board[0] or not words:
        return []

    # Build Trie
    root: dict = {}
    END = "#"
    for word in words:
        node = root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[END] = word

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return

        next_node = node[ch]

        # Found a word
        if END in next_node:
            result.append(next_node[END])
            del next_node[END]  # avoid duplicates

        # Mark as visited
        board[r][c] = "."

        # Explore 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != ".":
                dfs(nr, nc, next_node)

        # Restore
        board[r][c] = ch

        # Prune empty branches
        if not next_node:
            del node[ch]

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return sorted(result)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    rows = int(tokens[idx]); idx += 1
    cols = int(tokens[idx]); idx += 1
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(tokens[idx]); idx += 1
        board.append(row)
    n = int(tokens[idx]); idx += 1
    words = []
    for _ in range(n):
        words.append(tokens[idx]); idx += 1
    result = solve(board, words)
    print(" ".join(result))
