package ch19.solutions;

import java.util.*;

public class Practice03Sol {
    public static boolean solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[] color = new int[n];
        Arrays.fill(color, -1);
        for (int start = 0; start < n; start++) {
            if (color[start] != -1) continue;
            color[start] = 0;
            Queue<Integer> queue = new LinkedList<>();
            queue.add(start);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int nb : adj.get(node)) {
                    if (color[nb] == -1) {
                        color[nb] = 1 - color[node];
                        queue.add(nb);
                    } else if (color[nb] == color[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
