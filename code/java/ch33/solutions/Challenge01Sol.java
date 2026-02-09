package ch33.solutions;

import java.util.*;

public class Challenge01Sol {
    static int timer;

    public static int[][] solve(int n, int[][] connections) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : connections) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        int[] disc = new int[n], low = new int[n];
        Arrays.fill(disc, -1);
        List<int[]> bridges = new ArrayList<>();
        timer = 0;
        for (int i = 0; i < n; i++)
            if (disc[i] == -1) dfs(i, -1, adj, disc, low, bridges);

        bridges.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        return bridges.toArray(new int[0][]);
    }

    static void dfs(int u, int parent, List<List<Integer>> adj, int[] disc, int[] low, List<int[]> bridges) {
        disc[u] = low[u] = timer++;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                dfs(v, u, adj, disc, low, bridges);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u])
                    bridges.add(new int[]{Math.min(u,v), Math.max(u,v)});
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
