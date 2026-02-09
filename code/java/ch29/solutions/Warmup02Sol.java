package ch29.solutions;

public class Warmup02Sol {
    // Redundant Connection — 1-indexed nodes
    public static int[] solve(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1], rank = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int[] e : edges) {
            int rx = find(parent, e[0]), ry = find(parent, e[1]);
            if (rx == ry) return e;
            if (rank[rx] < rank[ry]) parent[rx] = ry;
            else if (rank[rx] > rank[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rank[rx]++; }
        }
        return new int[]{};
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
