package ch31.solutions;

import java.util.*;

public class Practice04Sol {
    // Tree Diameter via DP
    public static int solve(int n, int[][] edges) {
        if (n <= 1) return 0;

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        int[] depth = new int[n];
        int[] par = new int[n];
        Arrays.fill(par, -1);
        boolean[] visited = new boolean[n];
        List<Integer> order = new ArrayList<>();

        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int u = stack.pop();
            if (visited[u]) continue;
            visited[u] = true;
            order.add(u);
            for (int v : adj.get(u))
                if (!visited[v]) { par[v] = u; stack.push(v); }
        }

        int diameter = 0;
        for (int idx = order.size() - 1; idx >= 0; idx--) {
            int u = order.get(idx);
            int top1 = 0, top2 = 0;
            for (int v : adj.get(u)) {
                if (v == par[u]) continue;
                int d = depth[v] + 1;
                if (d >= top1) { top2 = top1; top1 = d; }
                else if (d > top2) top2 = d;
            }
            depth[u] = top1;
            diameter = Math.max(diameter, top1 + top2);
        }

        return diameter;
    }
}
