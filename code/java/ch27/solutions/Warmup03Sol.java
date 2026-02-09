package ch27.solutions;

import java.util.*;

public class Warmup03Sol {
    public static int[] solve(int n, int[][] edges, int src) {
        int INF = (int) 1e9;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;

        for (int i = 0; i < n - 1; i++)
            for (int[] e : edges)
                if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
                    dist[e[1]] = dist[e[0]] + e[2];

        return dist;
    }
}
