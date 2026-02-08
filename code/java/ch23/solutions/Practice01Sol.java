package ch23.solutions;

public class Practice01Sol {
    public static int solve(int[] costs, int k) {
        int n = costs.length;
        if (n <= 1) return n == 1 ? costs[0] : 0;
        int[] dp = new int[n];
        java.util.Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= Math.min(k, i); j++) {
                dp[i] = Math.min(dp[i], dp[i - j]);
            }
            dp[i] += costs[i];
        }
        return dp[n - 1];
    }
}
