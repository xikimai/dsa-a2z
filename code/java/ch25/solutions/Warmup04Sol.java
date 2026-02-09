package ch25.solutions;

public class Warmup04Sol {
    // Coin Change II: 1D DP, coins outer loop, forward iteration
    public static int solve(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins)
            for (int a = coin; a <= amount; a++)
                dp[a] += dp[a - coin];
        return dp[amount];
    }
}
