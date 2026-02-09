"""
Example 01: Grid DP Basics — From 1D to 2D
============================================
Chapter 24: Dynamic Programming II — Grids and Paths

This example demonstrates how 2D grid DP works:
  - Unique Paths: counting paths in a grid (combinatorics meets DP)
  - Minimum Path Sum: optimizing over a grid
  - Triangle: a non-rectangular grid DP
  - Filling a DP table row-by-row

All examples include the 2D table version and space-optimized 1D version.
"""


# ── Unique Paths (2D table) ─────────────────────────────────────────

def unique_paths_2d(m, n):
    """Count paths from (0,0) to (m-1,n-1) moving only right/down.
    O(m*n) time, O(m*n) space."""
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


# ── Unique Paths (space-optimized) ──────────────────────────────────

def unique_paths_1d(m, n):
    """Same problem, but O(n) space — only keep one row at a time."""
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


# ── Minimum Path Sum (2D table) ─────────────────────────────────────

def min_path_sum_2d(grid):
    """Find minimum-sum path from top-left to bottom-right.
    O(m*n) time, O(m*n) space."""
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


# ── Minimum Path Sum (space-optimized) ──────────────────────────────

def min_path_sum_1d(grid):
    """Same problem, O(n) space."""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[n - 1]


# ── Triangle Minimum Path Sum ───────────────────────────────────────

def triangle_min_total(triangle):
    """Find min path sum from top to bottom of a triangle.
    Bottom-up approach: start from the second-to-last row, O(n) space."""
    dp = triangle[-1][:]  # copy last row
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]


# ── Demo ─────────────────────────────────────────────────────────────

def demo_unique_paths():
    """Show unique paths with both 2D and 1D approaches."""
    print("=" * 60)
    print("UNIQUE PATHS: Counting Grid Paths")
    print("=" * 60)

    cases = [(3, 7, 28), (1, 1, 1), (3, 2, 3), (2, 3, 3)]
    for m, n, expected in cases:
        result_2d = unique_paths_2d(m, n)
        result_1d = unique_paths_1d(m, n)
        assert result_2d == result_1d == expected
        print(f"  ({m}, {n}) -> {result_2d} paths")


def demo_min_path_sum():
    """Show minimum path sum with both approaches."""
    print("\n" + "=" * 60)
    print("MINIMUM PATH SUM: Optimizing Over a Grid")
    print("=" * 60)

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result_2d = min_path_sum_2d(grid)
    result_1d = min_path_sum_1d(grid)
    assert result_2d == result_1d == 7
    print(f"  Grid: {grid}")
    print(f"  Min path sum: {result_2d}  (path: 1->3->1->1->1 = 7)")


def demo_triangle():
    """Show triangle minimum path sum."""
    print("\n" + "=" * 60)
    print("TRIANGLE: Non-Rectangular Grid DP")
    print("=" * 60)

    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    result = triangle_min_total(tri)
    assert result == 11
    print(f"  Triangle: {tri}")
    print(f"  Min path sum: {result}  (path: 2->3->5->1 = 11)")


if __name__ == "__main__":
    demo_unique_paths()
    demo_min_path_sum()
    demo_triangle()
