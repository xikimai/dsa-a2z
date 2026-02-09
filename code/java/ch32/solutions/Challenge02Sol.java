package ch32.solutions;

public class Challenge02Sol {
    public static String solve(String s) {
        if (s.length() <= 1) return s;

        String rev = new StringBuilder(s).reverse().toString();
        String combined = s + "#" + rev;

        int n = combined.length();
        int[] fail = new int[n];
        int length = 0, i = 1;
        while (i < n) {
            if (combined.charAt(i) == combined.charAt(length)) {
                fail[i++] = ++length;
            } else if (length > 0) {
                length = fail[length - 1];
            } else {
                fail[i++] = 0;
            }
        }

        int longestPalPrefix = fail[n - 1];
        String suffixToAdd = rev.substring(0, s.length() - longestPalPrefix);
        return suffixToAdd + s;
    }
}
