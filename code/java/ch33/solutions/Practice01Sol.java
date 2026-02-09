package ch33.solutions;

import java.util.*;

public class Practice01Sol {
    static int timer;

    public static int[] solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        int[] disc = new int[n], low = new int[n];
        Arrays.fill(disc, -1);
        Set<Integer> ap = new TreeSet<>();
        timer = 0;
        for (int i = 0; i < n; i++)
            if (disc[i] == -1) dfs(i, -1, adj, disc, low, ap);

        int[] result = new int[ap.size()];
        int idx = 0;
        for (int v : ap) result[idx++] = v;
        return result;
    }

    static void dfs(int u, int parent, List<List<Integer>> adj, int[] disc, int[] low, Set<Integer> ap) {
        disc[u] = low[u] = timer++;
        int children = 0;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                children++;
                dfs(v, u, adj, disc, low, ap);
                low[u] = Math.min(low[u], low[v]);
                if (parent == -1 && children > 1) ap.add(u);
                if (parent != -1 && low[v] >= disc[u]) ap.add(u);
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
