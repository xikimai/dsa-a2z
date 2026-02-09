package ch33.solutions;

import java.util.*;

public class Challenge04Sol {
    public static int solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>(), radj = new ArrayList<>();
        for (int i = 0; i < n; i++) { adj.add(new ArrayList<>()); radj.add(new ArrayList<>()); }
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); radj.get(e[1]).add(e[0]); }

        boolean[] visited = new boolean[n];
        List<Integer> order = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (!visited[i]) dfs1(i, adj, visited, order);

        int[] comp = new int[n];
        Arrays.fill(comp, -1);
        int count = 0;
        for (int i = order.size() - 1; i >= 0; i--)
            if (comp[order.get(i)] == -1)
                dfs2(order.get(i), count++, radj, comp);

        Set<Long> dagEdges = new HashSet<>();
        for (int[] e : edges) {
            if (comp[e[0]] != comp[e[1]]) {
                dagEdges.add((long)comp[e[0]] * n + comp[e[1]]);
            }
        }
        return dagEdges.size();
    }

    static void dfs1(int u, List<List<Integer>> adj, boolean[] vis, List<Integer> order) {
        vis[u] = true;
        for (int v : adj.get(u)) if (!vis[v]) dfs1(v, adj, vis, order);
        order.add(u);
    }

    static void dfs2(int u, int label, List<List<Integer>> radj, int[] comp) {
        comp[u] = label;
        for (int v : radj.get(u)) if (comp[v] == -1) dfs2(v, label, radj, comp);
    }
}
