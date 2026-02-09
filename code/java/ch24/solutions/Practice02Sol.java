package ch24.solutions;

import java.util.*;

public class Practice02Sol {
    public static int solve(int[][] matrix) {
        int n = matrix.length;
        int[] dp = matrix[0].clone();
        for (int i = 1; i < n; i++) {
            int[] newDp = new int[n];
            for (int j = 0; j < n; j++) {
                int best = dp[j];
                if (j > 0) best = Math.min(best, dp[j - 1]);
                if (j < n - 1) best = Math.min(best, dp[j + 1]);
                newDp[j] = matrix[i][j] + best;
            }
            dp = newDp;
        }
        int min = dp[0];
        for (int v : dp) min = Math.min(min, v);
        return min;
    }
}
