package ch25.learn;

/**
 * Example 02: String DP Basics — LCS and Edit Distance
 * ======================================================
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 *
 * Demonstrates LCS table construction and Edit Distance.
 */
public class Example02StringDpBasics {

    static int lcs(String a, String b) {
        int m = a.length(), n = b.length();
        int[] prev = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int[] curr = new int[n + 1];
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1))
                    curr[j] = prev[j - 1] + 1;
                else
                    curr[j] = Math.max(prev[j], curr[j - 1]);
            }
            prev = curr;
        }
        return prev[n];
    }

    static int editDistance(String a, String b) {
        int m = a.length(), n = b.length();
        int[] prev = new int[n + 1];
        for (int j = 0; j <= n; j++) prev[j] = j;
        for (int i = 1; i <= m; i++) {
            int[] curr = new int[n + 1];
            curr[0] = i;
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1))
                    curr[j] = prev[j - 1];
                else
                    curr[j] = 1 + Math.min(prev[j], Math.min(curr[j - 1], prev[j - 1]));
            }
            prev = curr;
        }
        return prev[n];
    }

    public static void main(String[] args) {
        System.out.println("LCS('abcde', 'ace') = " + lcs("abcde", "ace"));
        System.out.println("Edit Distance('horse', 'ros') = " + editDistance("horse", "ros"));
    }
}
