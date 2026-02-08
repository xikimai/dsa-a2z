"""
Solution for Challenge 3: N-Queens All Solutions
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Extend N-Queens count: when a complete placement is found, build
the board string representation and store it.

TIME COMPLEXITY:  O(n!)
SPACE COMPLEXITY: O(n^2) — storing solutions
"""


def solve(n: int) -> list[list[str]]:
    """Return all N-Queens solutions as lists of strings."""
    results = []
    queens = []  # queens[i] = column of queen in row i
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                row_str = '.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1)
                board.append(row_str)
            results.append(board)
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            queens.append(col)
            backtrack(row + 1)
            queens.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    results.sort()
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    result = solve(n)
    for solution in result:
        for row in solution:
            print(row)
        print()
