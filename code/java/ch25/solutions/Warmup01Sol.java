package ch25.solutions;

public class Warmup01Sol {
    // 0/1 Knapsack: space-optimized 1D DP, iterate backwards
    public static int solve(int[] weights, int[] values, int capacity) {
        int[] dp = new int[capacity + 1];
        for (int i = 0; i < weights.length; i++)
            for (int w = capacity; w >= weights[i]; w--)
                dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
        return dp[capacity];
    }
}
