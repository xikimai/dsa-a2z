package ch19.solutions;

import java.util.*;

public class Practice01Sol {
    public static int[] solve(int n, int[][] edges, int source) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[source] = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(source);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nb : adj.get(node)) {
                if (dist[nb] == -1) {
                    dist[nb] = dist[node] + 1;
                    queue.add(nb);
                }
            }
        }
        return dist;
    }
}
