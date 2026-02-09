package ch33.solutions;

import java.util.*;

public class Challenge02Sol {
    public static int solve(int n, int[][] connections) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] c : connections) {
            adj.get(c[0]).add(new int[]{c[1], 1}); // original: away
            adj.get(c[1]).add(new int[]{c[0], 0}); // reverse: toward
        }

        boolean[] visited = new boolean[n];
        visited[0] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int[] pair : adj.get(node)) {
                if (!visited[pair[0]]) {
                    visited[pair[0]] = true;
                    count += pair[1];
                    queue.add(pair[0]);
                }
            }
        }
        return count;
    }
}
