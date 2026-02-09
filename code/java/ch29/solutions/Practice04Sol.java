package ch29.solutions;

import java.util.*;

public class Practice04Sol {
    // Min Cost to Connect All Points — Kruskal's MST
    public static int solve(int[][] points) {
        int n = points.length;
        if (n <= 1) return 0;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                int dist = Math.abs(points[i][0] - points[j][0])
                         + Math.abs(points[i][1] - points[j][1]);
                edges.add(new int[]{dist, i, j});
            }
        edges.sort((a, b) -> a[0] - b[0]);

        int total = 0, count = 0;
        for (int[] e : edges) {
            int rx = find(parent, e[1]), ry = find(parent, e[2]);
            if (rx != ry) {
                if (rank[rx] < rank[ry]) parent[rx] = ry;
                else if (rank[rx] > rank[ry]) parent[ry] = rx;
                else { parent[ry] = rx; rank[rx]++; }
                total += e[0];
                if (++count == n - 1) break;
            }
        }
        return total;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
