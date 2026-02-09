package ch24.solutions;

import java.util.*;

public class Practice04Sol {
    public static int solve(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[n][n];
        for (int[] row : dp) Arrays.fill(row, -1);
        // Base: last row
        for (int c1 = 0; c1 < n; c1++)
            for (int c2 = 0; c2 < n; c2++)
                dp[c1][c2] = grid[m-1][c1] + (c1 != c2 ? grid[m-1][c2] : 0);
        for (int i = m - 2; i >= 0; i--) {
            int[][] newDp = new int[n][n];
            for (int[] row : newDp) Arrays.fill(row, -1);
            for (int c1 = 0; c1 < n; c1++) {
                for (int c2 = 0; c2 < n; c2++) {
                    int best = -1;
                    for (int d1 = -1; d1 <= 1; d1++)
                        for (int d2 = -1; d2 <= 1; d2++) {
                            int nc1 = c1 + d1, nc2 = c2 + d2;
                            if (nc1 >= 0 && nc1 < n && nc2 >= 0 && nc2 < n && dp[nc1][nc2] != -1)
                                best = Math.max(best, dp[nc1][nc2]);
                        }
                    if (best == -1) continue;
                    int val = grid[i][c1] + (c1 != c2 ? grid[i][c2] : 0);
                    newDp[c1][c2] = val + best;
                }
            }
            dp = newDp;
        }
        return dp[0][n - 1] != -1 ? dp[0][n - 1] : 0;
    }
}
