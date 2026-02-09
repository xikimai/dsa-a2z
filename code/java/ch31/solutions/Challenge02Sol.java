package ch31.solutions;

import java.util.*;

public class Challenge02Sol {
    // Number of Ways to Wear Hats — bitmask DP on people
    static final int MOD = 1_000_000_007;

    public static int solve(int n, int[][] hats) {
        List<List<Integer>> hatToPeople = new ArrayList<>();
        for (int i = 0; i <= 40; i++) hatToPeople.add(new ArrayList<>());
        for (int person = 0; person < n; person++)
            for (int hat : hats[person])
                hatToPeople.get(hat).add(person);

        int full = (1 << n) - 1;
        int[] dp = new int[1 << n];
        dp[0] = 1;

        for (int hat = 1; hat <= 40; hat++) {
            int[] newDp = Arrays.copyOf(dp, dp.length);
            for (int mask = 0; mask <= full; mask++) {
                if (dp[mask] == 0) continue;
                for (int person : hatToPeople.get(hat)) {
                    if ((mask & (1 << person)) != 0) continue;
                    int nm = mask | (1 << person);
                    newDp[nm] = (int) ((newDp[nm] + (long) dp[mask]) % MOD);
                }
            }
            dp = newDp;
        }

        return dp[full];
    }
}
