package ch31.solutions;

import java.util.*;

public class Practice02Sol {
    // Burst Balloons — interval DP
    public static int solve(int[] nums) {
        int n = nums.length + 2;
        int[] vals = new int[n];
        vals[0] = vals[n - 1] = 1;
        for (int i = 0; i < nums.length; i++) vals[i + 1] = nums[i];
        int[][] dp = new int[n][n];

        for (int len = 1; len <= n - 2; len++)
            for (int left = 1; left < n - len; left++) {
                int right = left + len - 1;
                for (int k = left; k <= right; k++) {
                    int coins = vals[left - 1] * vals[k] * vals[right + 1]
                              + dp[left][k - 1] + dp[k + 1][right];
                    dp[left][right] = Math.max(dp[left][right], coins);
                }
            }

        return dp[1][n - 2];
    }
}
