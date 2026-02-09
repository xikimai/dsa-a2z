package ch24.solutions;

import java.util.*;

public class Warmup02Sol {
    public static int solve(int[][] grid) {
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
}
