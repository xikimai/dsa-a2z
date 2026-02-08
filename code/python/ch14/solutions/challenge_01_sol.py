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
    if not matrix or not matrix[0]:
        return [0] * len(queries)

    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1]
                           - prefix[i-1][j-1] + matrix[i-1][j-1])

    result = []
    for r1, c1, r2, c2 in queries:
        total = (prefix[r2+1][c2+1] - prefix[r1][c2+1]
                - prefix[r2+1][c1] + prefix[r1][c1])
        result.append(total)
    return result


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
