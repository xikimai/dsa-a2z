package ch25.solutions;

public class Practice02Sol {
    // Unbounded Knapsack: iterate capacity forwards
    public static int solve(int[] weights, int[] values, int capacity) {
        int[] dp = new int[capacity + 1];
        for (int i = 0; i < weights.length; i++)
            for (int w = weights[i]; w <= capacity; w++)
                dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
        return dp[capacity];
    }
}
