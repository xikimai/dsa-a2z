package ch31.solutions;

import java.util.*;

public class Warmup03Sol {
    // House Robber on Tree — tree DP
    public static int solve(int n, int[] values, int[][] edges) {
        if (n == 0) return 0;
        if (n == 1) return values[0];

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        int[][] dp = new int[n][2];
        boolean[] visited = new boolean[n];
        int[] par = new int[n];
        Arrays.fill(par, -1);
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

        for (int idx = order.size() - 1; idx >= 0; idx--) {
            int u = order.get(idx);
            dp[u][1] = values[u];
            for (int v : adj.get(u)) {
                if (v == par[u]) continue;
                dp[u][0] += Math.max(dp[v][0], dp[v][1]);
                dp[u][1] += dp[v][0];
            }
        }

        return Math.max(dp[0][0], dp[0][1]);
    }
}
