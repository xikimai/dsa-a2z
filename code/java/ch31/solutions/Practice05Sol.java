package ch31.solutions;

import java.util.*;

public class Practice05Sol {
    // Count Numbers with Unique Digits — digit DP
    public static int solve(int n) {
        String s = Integer.toString(n);
        int len = s.length();
        int[] digits = new int[len];
        for (int i = 0; i < len; i++) digits[i] = s.charAt(i) - '0';

        Map<Long, Integer> memo = new HashMap<>();
        return dp(0, true, 0, false, digits, len, memo);
    }

    private static int dp(int pos, boolean tight, int mask, boolean started,
                           int[] digits, int len, Map<Long, Integer> memo) {
        if (pos == len) return started ? 1 : 0;

        long key = ((long) pos << 13) | ((tight ? 1L : 0L) << 12) | ((long) mask << 1) | (started ? 1L : 0L);
        if (memo.containsKey(key)) return memo.get(key);

        int limit = tight ? digits[pos] : 9;
        int count = 0;

        for (int d = 0; d <= limit; d++) {
            if (started && (mask & (1 << d)) != 0) continue;
            boolean newTight = tight && (d == limit);
            boolean newStarted = started || (d != 0);
            int newMask = newStarted ? (mask | (1 << d)) : mask;
            count += dp(pos + 1, newTight, newMask, newStarted, digits, len, memo);
        }

        memo.put(key, count);
        return count;
    }
}
