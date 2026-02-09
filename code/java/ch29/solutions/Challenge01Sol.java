package ch29.solutions;

public class Challenge01Sol {
    // Operations to Make Network Connected
    public static int solve(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;
        for (int[] c : connections) {
            int rx = find(parent, c[0]), ry = find(parent, c[1]);
            if (rx != ry) {
                if (rank[rx] < rank[ry]) parent[rx] = ry;
                else if (rank[rx] > rank[ry]) parent[ry] = rx;
                else { parent[ry] = rx; rank[rx]++; }
                components--;
            }
        }
        return components - 1;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
