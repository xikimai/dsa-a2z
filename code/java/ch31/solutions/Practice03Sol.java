package ch31.solutions;

import java.util.*;

public class Practice03Sol {
    // Minimum Score Triangulation — interval DP
    public static int solve(int[] values) {
        int n = values.length;
        if (n < 3) return 0;
        int[][] dp = new int[n][n];

        for (int len = 3; len <= n; len++)
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i + 1; k < j; k++) {
                    int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }

        return dp[0][n - 1];
    }
}
