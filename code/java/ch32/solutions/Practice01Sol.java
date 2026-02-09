package ch32.solutions;

import java.util.*;

public class Practice01Sol {
    public static List<Integer> solve(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        if (m == 0 || m > n) return matches;

        long BASE = 131, MOD = 1_000_000_007;
        long pHash = 0, tHash = 0, power = 1;
        for (int i = 0; i < m - 1; i++) power = power * BASE % MOD;

        for (int i = 0; i < m; i++) {
            pHash = (pHash * BASE + pattern.charAt(i)) % MOD;
            tHash = (tHash * BASE + text.charAt(i)) % MOD;
        }

        for (int i = 0; i <= n - m; i++) {
            if (pHash == tHash && text.substring(i, i + m).equals(pattern))
                matches.add(i);
            if (i < n - m)
                tHash = ((tHash - text.charAt(i) * power % MOD + MOD)
                         * BASE + text.charAt(i + m)) % MOD;
        }
        return matches;
    }
}
