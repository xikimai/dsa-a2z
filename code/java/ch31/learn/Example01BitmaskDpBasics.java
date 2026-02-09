package ch31.learn;

import java.util.*;

/**
 * Example 01: Bitmask DP Basics — Subset Encoding & TSP
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
public class Example01BitmaskDpBasics {

    /** Show which items are in the subset represented by mask. */
    static List<Integer> showSubset(int mask, int n) {
        List<Integer> items = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if ((mask & (1 << i)) != 0) items.add(i);
        return items;
    }

    /** TSP using bitmask DP. Returns min cost Hamiltonian cycle from city 0. */
    static int tsp(int n, int[][] dist) {
        int full = (1 << n) - 1;
        int INF = Integer.MAX_VALUE / 2;
        int[][] dp = new int[1 << n][n];
        for (int[] row : dp) Arrays.fill(row, INF);
        dp[1][0] = 0;

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
            ans = Math.min(ans, dp[full][u] + dist[u][0]);
        return ans;
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("BITMASK BASICS: Subset Encoding");
        System.out.println("=".repeat(60));

        int n = 4;
        System.out.println("\nAll subsets of {0,1,2,3}:");
        for (int mask = 0; mask < (1 << n); mask++)
            System.out.printf("  mask=%s (decimal %d) -> %s%n",
                String.format("%" + n + "s", Integer.toBinaryString(mask)).replace(' ', '0'),
                mask, showSubset(mask, n));

        System.out.println("\n" + "=".repeat(60));
        System.out.println("TRAVELING SALESMAN PROBLEM (TSP)");
        System.out.println("=".repeat(60));

        int[][] dist = {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}};
        System.out.println("  Min TSP tour cost (4 cities): " + tsp(4, dist));
    }
}
