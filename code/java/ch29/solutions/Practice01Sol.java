package ch29.solutions;

public class Practice01Sol {
    // Number of Provinces
    public static int solve(int[][] isConnected) {
        int n = isConnected.length;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (isConnected[i][j] == 1) {
                    int rx = find(parent, i), ry = find(parent, j);
                    if (rx != ry) {
                        if (rank[rx] < rank[ry]) parent[rx] = ry;
                        else if (rank[rx] > rank[ry]) parent[ry] = rx;
                        else { parent[ry] = rx; rank[rx]++; }
                        components--;
                    }
                }
        return components;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
