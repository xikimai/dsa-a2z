package ch32.learn;

import java.util.*;

/**
 * Example 02: KMP and Z-Function Demo
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
public class Example02KmpDemo {

    static int[] buildFailure(String pattern) {
        int m = pattern.length();
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
        return fail;
    }

    static List<Integer> kmpSearch(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        if (m == 0) return matches;
        int[] fail = buildFailure(pattern);
        int j = 0;
        for (int i = 0; i < n; i++) {
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

    static int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i < r) z[i] = Math.min(r - i, z[i - l]);
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i]))
                z[i]++;
            if (i + z[i] > r) { l = i; r = i + z[i]; }
        }
        return z;
    }

    public static void main(String[] args) {
        System.out.println("KMP AND Z-FUNCTION DEMO");

        String pattern = "AABAAAB";
        int[] fail = buildFailure(pattern);
        System.out.println("  Pattern: " + pattern);
        System.out.println("  Failure: " + Arrays.toString(fail));

        String text = "AABAACAADAABAABA";
        List<Integer> matches = kmpSearch(text, "AABA");
        System.out.println("  KMP matches: " + matches);

        String s = "aabxaa";
        int[] z = zFunction(s);
        System.out.println("  Z-array of '" + s + "': " + Arrays.toString(z));
    }
}
