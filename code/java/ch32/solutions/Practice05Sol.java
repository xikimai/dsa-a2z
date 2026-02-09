package ch32.solutions;

public class Practice05Sol {
    public static String solve(String s) {
        int n = s.length();
        if (n <= 1) return "";

        int[] fail = new int[n];
        int length = 0, i = 1;
        while (i < n) {
            if (s.charAt(i) == s.charAt(length)) {
                fail[i++] = ++length;
            } else if (length > 0) {
                length = fail[length - 1];
            } else {
                fail[i++] = 0;
            }
        }
        return s.substring(0, fail[n - 1]);
    }
}
