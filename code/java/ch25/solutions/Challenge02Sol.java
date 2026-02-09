package ch25.solutions;

public class Challenge02Sol {
    // Rod Cutting: unbounded knapsack
    public static int solve(int[] prices) {
        int n = prices.length;
        int[] dp = new int[n + 1];
        for (int len = 1; len <= n; len++)
            for (int k = 1; k <= len; k++)
                dp[len] = Math.max(dp[len], dp[len - k] + prices[k - 1]);
        return dp[n];
    }
}
