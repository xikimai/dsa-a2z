package ch19.solutions;

import java.util.*;

public class Warmup02Sol {
    public static List<Integer> solve(int n, int[][] edges, int source) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] visited = new boolean[n];
        visited[source] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(source);
        List<Integer> order = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            order.add(node);
            List<Integer> nbrs = new ArrayList<>(adj.get(node));
            Collections.sort(nbrs);
            for (int nb : nbrs) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    queue.add(nb);
                }
            }
        }
        return order;
    }
}
