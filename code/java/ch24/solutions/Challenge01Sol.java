package ch24.solutions;

import java.util.*;

public class Challenge01Sol {
    public static int solve(int[][] dungeon) {
        int m = dungeon.length, n = dungeon[0].length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n - 1] = 1;
        for (int i = m - 1; i >= 0; i--) {
            int[] newDp = new int[n + 1];
            Arrays.fill(newDp, Integer.MAX_VALUE);
            for (int j = n - 1; j >= 0; j--) {
                int minNext = Math.min(dp[j], newDp[j + 1]);
                newDp[j] = Math.max(1, minNext - dungeon[i][j]);
            }
            dp = newDp;
        }
        return dp[0];
    }
}
