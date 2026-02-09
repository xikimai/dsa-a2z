package ch27.solutions;

import java.util.*;

public class Practice01Sol {
    public static int solve(int n, int[][] flights, int src, int dst, int k) {
        int INF = (int) 1e9;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;

        for (int i = 0; i <= k; i++) {
            int[] prev = dist.clone();
            for (int[] f : flights)
                if (prev[f[0]] != INF && prev[f[0]] + f[2] < dist[f[1]])
                    dist[f[1]] = prev[f[0]] + f[2];
        }
        return dist[dst] >= INF ? -1 : dist[dst];
    }
}
