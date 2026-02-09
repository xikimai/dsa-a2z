package ch33.solutions;

import java.util.*;

public class Warmup01Sol {
    public static int[] solve(int n, int[][] edges, int[][] queries) {
        if (n == 1) {
            int[] res = new int[queries.length];
            return res;
        }
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        int LOG = Math.max(1, (int)(Math.ceil(Math.log(n) / Math.log(2))) + 1);
        int[][] up = new int[n][LOG];
        int[] depth = new int[n];
        for (int[] row : up) Arrays.fill(row, -1);

        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0); visited[0] = true;
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
                if (up[v][k-1] != -1) up[v][k] = up[up[v][k-1]][k-1];

        int[] result = new int[queries.length];
        for (int q = 0; q < queries.length; q++)
            result[q] = lca(queries[q][0], queries[q][1], up, depth, LOG);
        return result;
    }

    static int lca(int u, int v, int[][] up, int[] depth, int LOG) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if (((diff >> k) & 1) == 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    }
}
