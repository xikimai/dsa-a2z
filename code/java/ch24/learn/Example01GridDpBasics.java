package ch24.learn;

import java.util.*;

/**
 * Example 01: Grid DP Basics — From 1D to 2D
 * Chapter 24: Dynamic Programming II — Grids and Paths
 *
 * Demonstrates: unique paths, min path sum, triangle (2D and 1D approaches)
 */
public class Example01GridDpBasics {

    // Unique Paths (space-optimized)
    static int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                dp[j] += dp[j - 1];
        return dp[n - 1];
    }

    // Minimum Path Sum (space-optimized)
    static int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[n];
        dp[0] = grid[0][0];
        for (int j = 1; j < n; j++) dp[j] = dp[j - 1] + grid[0][j];
        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++)
                dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
        }
        return dp[n - 1];
    }

    // Triangle (bottom-up, O(n) space)
    static int triangleMinTotal(int[][] tri) {
        int n = tri.length;
        int[] dp = tri[n - 1].clone();
        for (int i = n - 2; i >= 0; i--)
            for (int j = 0; j <= i; j++)
                dp[j] = tri[i][j] + Math.min(dp[j], dp[j + 1]);
        return dp[0];
    }

    public static void main(String[] args) {
        System.out.println("Unique Paths (3,7) = " + uniquePaths(3, 7));
        System.out.println("Min Path Sum = " + minPathSum(new int[][]{{1,3,1},{1,5,1},{4,2,1}}));
        System.out.println("Triangle Min = " + triangleMinTotal(new int[][]{{2},{3,4},{6,5,7},{4,1,8,3}}));
    }
}
