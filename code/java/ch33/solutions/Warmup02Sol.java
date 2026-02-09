package ch33.solutions;

import java.util.*;

public class Warmup02Sol {
    public static int[] solve(int n, int[][] edges) {
        if (n == 1) return new int[]{0};
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }
        for (List<Integer> list : adj) Collections.sort(list);

        int[] order = new int[n];
        boolean[] visited = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0); visited[0] = true;
        int idx = 0;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order[idx++] = node;
            List<Integer> neighbors = adj.get(node);
            for (int i = neighbors.size() - 1; i >= 0; i--) {
                int nb = neighbors.get(i);
                if (!visited[nb]) { visited[nb] = true; stack.push(nb); }
            }
        }
        return order;
    }
}
