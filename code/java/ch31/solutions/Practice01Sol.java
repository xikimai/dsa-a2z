package ch31.solutions;

import java.util.*;

public class Practice01Sol {
    // Shortest Hamiltonian Path — bitmask DP, no return
    public static int solve(int n, int[][] dist) {
        int INF = Integer.MAX_VALUE / 2;
        int full = (1 << n) - 1;
        int[][] dp = new int[1 << n][n];
        for (int[] row : dp) Arrays.fill(row, INF);

        for (int i = 0; i < n; i++)
            dp[1 << i][i] = 0;

        for (int mask = 1; mask <= full; mask++)
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] >= INF) continue;
                if ((mask & (1 << u)) == 0) continue;
                for (int v = 0; v < n; v++) {
                    if ((mask & (1 << v)) != 0) continue;
                    int nm = mask | (1 << v);
                    dp[nm][v] = Math.min(dp[nm][v], dp[mask][u] + dist[u][v]);
                }
            }

        int ans = INF;
        for (int u = 0; u < n; u++)
            ans = Math.min(ans, dp[full][u]);
        return ans;
    }
}
