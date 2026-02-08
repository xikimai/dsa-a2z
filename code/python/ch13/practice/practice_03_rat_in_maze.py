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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    result = solve(maze)
    for path in result:
        print(path)

