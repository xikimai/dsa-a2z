package ch24.solutions;

import java.util.*;

public class Challenge04Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        if (n == 0 || grid[0][0] == -1 || grid[n-1][n-1] == -1) return 0;
        int NEG = Integer.MIN_VALUE / 2;
        int[][] dp = new int[n][n];
        for (int[] row : dp) Arrays.fill(row, NEG);
        dp[0][0] = grid[0][0];
        int maxT = 2 * (n - 1);
        for (int t = 1; t <= maxT; t++) {
            int[][] newDp = new int[n][n];
            for (int[] row : newDp) Arrays.fill(row, NEG);
            int rLo = Math.max(0, t - (n - 1));
            int rHi = Math.min(n - 1, t);
            for (int r1 = rLo; r1 <= rHi; r1++) {
                int c1 = t - r1;
                if (c1 < 0 || c1 >= n || grid[r1][c1] == -1) continue;
                for (int r2 = rLo; r2 <= rHi; r2++) {
                    int c2 = t - r2;
                    if (c2 < 0 || c2 >= n || grid[r2][c2] == -1) continue;
                    int best = NEG;
                    for (int pr1 : new int[]{r1, r1-1})
                        for (int pr2 : new int[]{r2, r2-1})
                            if (pr1 >= 0 && pr2 >= 0 && pr1 < n && pr2 < n)
                                best = Math.max(best, dp[pr1][pr2]);
                    if (best == NEG) continue;
                    int cherries = grid[r1][c1];
                    if (r1 != r2) cherries += grid[r2][c2];
                    newDp[r1][r2] = best + cherries;
                }
            }
            dp = newDp;
        }
        return Math.max(0, dp[n-1][n-1]);
    }
}
