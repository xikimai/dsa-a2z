package ch31.solutions;

import java.util.*;

public class Challenge01Sol {
    // Minimum Cost to Merge Stones — interval DP
    public static int solve(int[] stones, int k) {
        int n = stones.length;
        if ((n - 1) % (k - 1) != 0) return -1;
        if (n == 1) return 0;

        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];

        int INF = Integer.MAX_VALUE / 2;
        int[][] dp = new int[n][n];

        for (int len = 2; len <= n; len++)
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = INF;
                for (int mid = i; mid < j; mid += k - 1)
                    dp[i][j] = Math.min(dp[i][j], dp[i][mid] + dp[mid + 1][j]);
                if ((j - i) % (k - 1) == 0)
                    dp[i][j] += prefix[j + 1] - prefix[i];
            }

        return dp[0][n - 1];
    }
}
