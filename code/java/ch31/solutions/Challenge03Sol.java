package ch31.solutions;

import java.util.*;

public class Challenge03Sol {
    // Binary Tree Cameras — tree DP with 3 states
    static final int INF = 1_000_000;

    public static int solve(int n, int[][] edges) {
        if (n == 0) return 0;
        if (n <= 2) return 1;

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        // dp[u][0] = not covered, dp[u][1] = covered no camera, dp[u][2] = has camera
        int[][] dp = new int[n][3];
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
            List<Integer> children = new ArrayList<>();
            for (int v : adj.get(u)) if (v != par[u]) children.add(v);

            if (children.isEmpty()) {
                dp[u][0] = 0;
                dp[u][1] = INF;
                dp[u][2] = 1;
                continue;
            }

            // State 2: has camera
            int cam = 1;
            for (int v : children)
                cam += Math.min(dp[v][0], Math.min(dp[v][1], dp[v][2]));

            // State 0: not covered
            int notCov = 0;
            for (int v : children)
                notCov += Math.min(dp[v][1], dp[v][2]);

            // State 1: covered by child
            int base = 0;
            for (int v : children)
                base += Math.min(dp[v][1], dp[v][2]);

            int cov = INF;
            boolean allPrefer1 = true;
            for (int v : children)
                if (dp[v][2] <= dp[v][1]) { allPrefer1 = false; break; }

            if (!allPrefer1) {
                cov = base;
            } else {
                int minUpgrade = INF;
                for (int v : children)
                    minUpgrade = Math.min(minUpgrade, dp[v][2] - dp[v][1]);
                cov = base + minUpgrade;
            }

            dp[u][0] = notCov;
            dp[u][1] = cov;
            dp[u][2] = cam;
        }

        return Math.min(dp[0][1], dp[0][2]);
    }
}
