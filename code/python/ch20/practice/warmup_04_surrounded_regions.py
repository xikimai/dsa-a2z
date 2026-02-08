"""
Warmup 4: Surrounded Regions
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n board of 'X' and 'O', capture all regions that are
completely surrounded by 'X'. A region is surrounded if none of its
cells are on the border of the board or connected to a border cell.
Flip surrounded 'O's to 'X'.

EXAMPLES
--------
>>> solve([['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']])
[['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]

CONSTRAINTS
-----------
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'
"""


def solve(board: list[list[str]]) -> list[list[str]]:
    """Capture surrounded regions in-place and return the board."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    board = []
    for _ in range(rows):
        board.append(input().split())
    solve(board)
    for row in board:
        print(" ".join(row))
