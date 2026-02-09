package ch24.solutions;

import java.util.*;

public class Practice03Sol {
    public static int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length;
        int[] dp = new int[n];
        int maxSide = 0, prevDiag = 0;
        for (int i = 0; i < m; i++) {
            prevDiag = 0;
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
}
