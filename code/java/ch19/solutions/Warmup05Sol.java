package ch19.solutions;

import java.util.*;

public class Warmup05Sol {
    public static boolean solve(int n, int[][] edges, int source, int dest) {
        if (source == dest) return true;
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
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nb : adj.get(node)) {
                if (nb == dest) return true;
                if (!visited[nb]) {
                    visited[nb] = true;
                    queue.add(nb);
                }
            }
        }
        return false;
    }
}
