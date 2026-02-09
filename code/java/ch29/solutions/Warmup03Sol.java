package ch29.solutions;

import java.util.*;

public class Warmup03Sol {
    // Kruskal's MST
    public static int solve(int n, int[][] edges) {
        if (n <= 1) return 0;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        Arrays.sort(edges, (a, b) -> a[2] - b[2]);
        int total = 0;
        for (int[] e : edges) {
            int rx = find(parent, e[0]), ry = find(parent, e[1]);
            if (rx != ry) {
                if (rank[rx] < rank[ry]) parent[rx] = ry;
                else if (rank[rx] > rank[ry]) parent[ry] = rx;
                else { parent[ry] = rx; rank[rx]++; }
                total += e[2];
            }
        }
        return total;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
