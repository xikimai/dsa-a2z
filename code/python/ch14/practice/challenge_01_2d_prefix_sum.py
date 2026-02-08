"""
Solution for Challenge 1: 2D Prefix Sum and Range Query
========================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Build 2D prefix sum with inclusion-exclusion.
Answer each query in O(1).

TIME COMPLEXITY:  O(rows * cols + q)
SPACE COMPLEXITY: O(rows * cols) — 2D prefix array
"""


def solve(matrix: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return list of rectangle sums for each query."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    print(solve(matrix, queries))

