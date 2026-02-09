package ch24.learn;

import java.util.*;

/**
 * Example 02: Space Optimization — Reducing 2D DP to 1D
 * Chapter 24: Dynamic Programming II — Grids and Paths
 *
 * Demonstrates: unique paths with obstacles, maximal square, count squares
 */
public class Example02SpaceOptimization {

    // Unique Paths with Obstacles
    static int uniquePathsObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] == 1) return 0;
        int[] dp = new int[n];
        dp[0] = 1;
        for (int j = 1; j < n; j++) dp[j] = grid[0][j] == 0 ? dp[j - 1] : 0;
        for (int i = 1; i < m; i++) {
            dp[0] = grid[i][0] == 0 ? dp[0] : 0;
            for (int j = 1; j < n; j++)
                dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j - 1];
        }
        return dp[n - 1];
    }

    // Maximal Square (space-optimized)
    static int maximalSquare(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[] dp = new int[n];
        int maxSide = 0, prevDiag = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int temp = dp[j];
                if (matrix[i][j] == 1) {
                    dp[j] = (i == 0 || j == 0) ? 1 : Math.min(Math.min(dp[j], dp[j-1]), prevDiag) + 1;
                    maxSide = Math.max(maxSide, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prevDiag = temp;
            }
        }
        return maxSide * maxSide;
    }

    public static void main(String[] args) {
        System.out.println("Obstacles: " + uniquePathsObstacles(new int[][]{{0,0,0},{0,1,0},{0,0,0}}));
        System.out.println("Maximal Square: " + maximalSquare(new int[][]{{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}}));
    }
}
