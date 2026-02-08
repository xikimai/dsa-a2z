package ch19.solutions;

import java.util.*;

public class Practice02Sol {
    public static boolean solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] visited = new boolean[n];
        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                if (dfs(adj, v, -1, visited)) return true;
            }
        }
        return false;
    }

    private static boolean dfs(List<List<Integer>> adj, int node, int parent, boolean[] visited) {
        visited[node] = true;
        for (int nb : adj.get(node)) {
            if (!visited[nb]) {
                if (dfs(adj, nb, node, visited)) return true;
            } else if (nb != parent) {
                return true;
            }
        }
        return false;
    }
}
