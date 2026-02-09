package ch33.solutions;

import java.util.*;

public class Practice05Sol {
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

        int[] sizes = new int[count];
        for (int c : comp) sizes[c]++;
        int result = 0;
        for (int s : sizes) if (s > 1) result++;
        return result;
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
