package ch19.solutions;

import java.util.*;

public class Warmup04Sol {
    public static int solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] visited = new boolean[n];
        int count = 0;
        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                Queue<Integer> queue = new LinkedList<>();
                queue.add(v);
                visited[v] = true;
                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    for (int nb : adj.get(node)) {
                        if (!visited[nb]) {
                            visited[nb] = true;
                            queue.add(nb);
                        }
                    }
                }
                count++;
            }
        }
        return count;
    }
}
