package ch31.learn;

import java.util.*;

/**
 * Example 02: Interval DP Demo — MCM & Burst Balloons
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
public class Example02IntervalDpDemo {

    /** Matrix Chain Multiplication — interval DP, O(n^3). */
    static int mcm(int[] dims) {
        int n = dims.length - 1;
        if (n <= 1) return 0;
        int[][] dp = new int[n][n];
        for (int len = 2; len <= n; len++)
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        return dp[0][n - 1];
    }

    /** Burst Balloons — interval DP, O(n^3). */
    static int burstBalloons(int[] nums) {
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

    public static void main(String[] args) {
        System.out.println("MCM [10,30,5,60] = " + mcm(new int[]{10,30,5,60}));
        System.out.println("Burst [3,1,5,8] = " + burstBalloons(new int[]{3,1,5,8}));
    }
}
