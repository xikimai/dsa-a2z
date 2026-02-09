package ch31.solutions;

import java.util.*;

public class Challenge04Sol {
    // Palindrome Partitioning II
    public static int solve(String s) {
        int n = s.length();
        if (n <= 1) return 0;

        boolean[][] isPal = new boolean[n][n];
        for (int i = 0; i < n; i++) isPal[i][i] = true;
        for (int i = 0; i < n - 1; i++) isPal[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));
        for (int len = 3; len <= n; len++)
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                isPal[i][j] = (s.charAt(i) == s.charAt(j)) && isPal[i + 1][j - 1];
            }

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            if (isPal[0][i]) {
                dp[i] = 0;
            } else {
                dp[i] = i;
                for (int j = 1; j <= i; j++)
                    if (isPal[j][i])
                        dp[i] = Math.min(dp[i], dp[j - 1] + 1);
            }
        }

        return dp[n - 1];
    }
}
