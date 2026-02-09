"""
Example 02: Space Optimization — Reducing 2D DP to 1D
======================================================
Chapter 24: Dynamic Programming II — Grids and Paths

The key insight: when filling a 2D DP table row by row, and each cell
only depends on the current row and the previous row, you only need
to keep ONE row in memory. This reduces space from O(m*n) to O(n).

This example demonstrates the technique on three problems:
  - Unique Paths with Obstacles
  - Maximal Square (DP on squares)
  - Count Square Submatrices
"""


# ── Unique Paths with Obstacles ─────────────────────────────────────

def unique_paths_obstacles_2d(grid):
    """2D table approach: O(m*n) space."""
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) if grid[i][j] == 0 else 0
    return dp[m - 1][n - 1]


def unique_paths_obstacles_1d(grid):
    """Space-optimized: O(n) space."""
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0
    dp = [0] * n
    dp[0] = 1
    for j in range(1, n):
        dp[j] = dp[j - 1] if grid[0][j] == 0 else 0
    for i in range(1, m):
        dp[0] = dp[0] if grid[i][0] == 0 else 0
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[j] = 0
            else:
                dp[j] += dp[j - 1]
    return dp[n - 1]


# ── Maximal Square ──────────────────────────────────────────────────

def maximal_square_2d(matrix):
    """Find the largest square of all 1s. Return its AREA.
    dp[i][j] = side length of largest square with bottom-right at (i,j).
    O(m*n) space."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side


def maximal_square_1d(matrix):
    """Space-optimized: O(n) space."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    max_side = 0
    prev_diag = 0  # dp[i-1][j-1]
    for i in range(m):
        for j in range(n):
            temp = dp[j]  # save before overwriting (becomes prev_diag for next j)
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev_diag) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev_diag = temp
    return max_side * max_side


# ── Count Square Submatrices ────────────────────────────────────────

def count_squares(matrix):
    """Count ALL square submatrices with all ones.
    Same recurrence as maximal square, but SUM all dp values.
    O(m*n) time, O(n) space."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    total = 0
    prev_diag = 0
    for i in range(m):
        for j in range(n):
            temp = dp[j]
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev_diag) + 1
                total += dp[j]
            else:
                dp[j] = 0
            prev_diag = temp
    return total


# ── Demo ─────────────────────────────────────────────────────────────

def demo_obstacles():
    """Show unique paths with obstacles."""
    print("=" * 60)
    print("UNIQUE PATHS WITH OBSTACLES: 2D vs 1D")
    print("=" * 60)

    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    r2d = unique_paths_obstacles_2d(grid)
    r1d = unique_paths_obstacles_1d(grid)
    assert r2d == r1d == 2
    print(f"  Grid (0=open, 1=blocked):")
    for row in grid:
        print(f"    {row}")
    print(f"  Paths: {r2d}")


def demo_maximal_square():
    """Show maximal square."""
    print("\n" + "=" * 60)
    print("MAXIMAL SQUARE: DP on Squares")
    print("=" * 60)

    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]
    r2d = maximal_square_2d(matrix)
    r1d = maximal_square_1d(matrix)
    assert r2d == r1d == 4
    print(f"  Matrix:")
    for row in matrix:
        print(f"    {row}")
    print(f"  Largest square area: {r2d}  (2x2 square)")


def demo_count_squares():
    """Show count square submatrices."""
    print("\n" + "=" * 60)
    print("COUNT SQUARE SUBMATRICES")
    print("=" * 60)

    matrix = [[0, 1, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1]]
    result = count_squares(matrix)
    assert result == 15
    print(f"  Matrix:")
    for row in matrix:
        print(f"    {row}")
    print(f"  Total square submatrices: {result}")


if __name__ == "__main__":
    demo_obstacles()
    demo_maximal_square()
    demo_count_squares()
