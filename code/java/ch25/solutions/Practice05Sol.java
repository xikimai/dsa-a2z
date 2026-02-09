package ch25.solutions;

public class Practice05Sol {
    // Distinct Subsequences: space-optimized 1D DP, iterate backwards
    public static int solve(String s, String t) {
        int m = s.length(), n = t.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = Math.min(i, n); j >= 1; j--)
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    dp[j] += dp[j - 1];
        return dp[n];
    }
}
