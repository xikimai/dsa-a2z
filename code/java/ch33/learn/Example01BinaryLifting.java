package ch33.learn;

import java.util.*;

/**
 * Example 01: Binary Lifting — LCA in O(log n)
 * Chapter 33: Advanced Trees & Graph Algorithms
 */
public class Example01BinaryLifting {

    static int[][] up;
    static int[] depth;
    static int LOG;

    static void build(int n, int[][] edges, int root) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        LOG = Math.max(1, (int)(Math.ceil(Math.log(n) / Math.log(2))) + 1);
        up = new int[n][LOG];
        depth = new int[n];
        for (int[] row : up) Arrays.fill(row, -1);

        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(root);
        visited[root] = true;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nb : adj.get(node)) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = depth[node] + 1;
                    up[nb][0] = node;
                    queue.add(nb);
                }
            }
        }

        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (up[v][k - 1] != -1)
                    up[v][k] = up[up[v][k - 1]][k - 1];
    }

    static int lca(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if (((diff >> k) & 1) == 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    }

    public static void main(String[] args) {
        int n = 7;
        int[][] edges = {{0,1},{0,2},{1,3},{1,4},{2,5},{5,6}};
        build(n, edges, 0);

        System.out.println("Binary Lifting: LCA Demo");
        System.out.printf("  LCA(3,4) = %d%n", lca(3, 4)); // 1
        System.out.printf("  LCA(3,6) = %d%n", lca(3, 6)); // 0
        System.out.printf("  LCA(4,5) = %d%n", lca(4, 5)); // 0
    }
}
