package ch25.solutions;

public class Practice06Sol {
    // Wildcard Matching: space-optimized 2-row DP
    public static boolean solve(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[] prev = new boolean[n + 1];
        prev[0] = true;
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == '*') prev[j] = prev[j - 1];
            else break;
        }
        for (int i = 1; i <= m; i++) {
            boolean[] curr = new boolean[n + 1];
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*')
                    curr[j] = curr[j - 1] || prev[j];
                else if (p.charAt(j - 1) == '?' || s.charAt(i - 1) == p.charAt(j - 1))
                    curr[j] = prev[j - 1];
            }
            prev = curr;
        }
        return prev[n];
    }
}
