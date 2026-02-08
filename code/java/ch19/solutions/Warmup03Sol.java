package ch19.solutions;

import java.util.*;

public class Warmup03Sol {
    public static List<Integer> solve(int n, int[][] edges, int source) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] visited = new boolean[n];
        List<Integer> order = new ArrayList<>();
        dfs(adj, source, visited, order);
        return order;
    }

    private static void dfs(List<List<Integer>> adj, int node,
                             boolean[] visited, List<Integer> order) {
        visited[node] = true;
        order.add(node);
        List<Integer> nbrs = new ArrayList<>(adj.get(node));
        Collections.sort(nbrs);
        for (int nb : nbrs) {
            if (!visited[nb]) dfs(adj, nb, visited, order);
        }
    }
}
