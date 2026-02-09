package ch28.solutions;

import java.util.*;

public class Practice04Sol {
    // All Ancestors of a Node
    public static List<List<Integer>> solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);

        Set<Integer>[] ancestors = new Set[n];
        for (int i = 0; i < n; i++) ancestors[i] = new TreeSet<>();

        // For each node u, DFS forward and add u as ancestor of reachable nodes
        for (int u = 0; u < n; u++) {
            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(u);
            boolean[] visited = new boolean[n];
            while (!stack.isEmpty()) {
                int node = stack.pop();
                for (int v : adj.get(node)) {
                    if (!visited[v]) {
                        visited[v] = true;
                        ancestors[v].add(u);
                        stack.push(v);
                    }
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n; i++) result.add(new ArrayList<>(ancestors[i]));
        return result;
    }
}
