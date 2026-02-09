package ch32.solutions;

import java.util.*;

public class Warmup03Sol {
    public static List<Integer> solve(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        if (m == 0) return matches;

        // Build failure function
        int[] fail = new int[m];
        int length = 0, i = 1;
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                fail[i++] = ++length;
            } else if (length > 0) {
                length = fail[length - 1];
            } else {
                fail[i++] = 0;
            }
        }

        // Search
        int j = 0;
        for (i = 0; i < n; i++) {
            while (j > 0 && text.charAt(i) != pattern.charAt(j))
                j = fail[j - 1];
            if (text.charAt(i) == pattern.charAt(j)) j++;
            if (j == m) {
                matches.add(i - m + 1);
                j = fail[j - 1];
            }
        }
        return matches;
    }
}
