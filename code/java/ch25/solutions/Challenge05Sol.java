package ch25.solutions;

public class Challenge05Sol {
    // Min Insertions for Palindrome: n - LCS(s, reverse(s))
    public static int solve(String s) {
        int n = s.length();
        String t = new StringBuilder(s).reverse().toString();
        int[] prev = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int[] curr = new int[n + 1];
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    curr[j] = prev[j - 1] + 1;
                else
                    curr[j] = Math.max(prev[j], curr[j - 1]);
            }
            prev = curr;
        }
        return n - prev[n];
    }
}
