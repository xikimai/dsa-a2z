package ch33.learn;

import java.util.*;

/**
 * Example 02: Tarjan's Bridges & Kosaraju's SCC
 * Chapter 33: Advanced Trees & Graph Algorithms
 */
public class Example02TarjanKosaraju {

    // ── Tarjan's Bridges ─────────────────────────────────────
    static int timer = 0;

    static List<int[]> findBridges(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[] disc = new int[n], low = new int[n];
        Arrays.fill(disc, -1);
        List<int[]> bridges = new ArrayList<>();
        timer = 0;
        for (int i = 0; i < n; i++)
            if (disc[i] == -1) dfsBridge(i, -1, adj, disc, low, bridges);
        return bridges;
    }

    static void dfsBridge(int u, int parent, List<List<Integer>> adj, int[] disc, int[] low, List<int[]> bridges) {
        disc[u] = low[u] = timer++;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                dfsBridge(v, u, adj, disc, low, bridges);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u])
                    bridges.add(new int[]{Math.min(u,v), Math.max(u,v)});
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }

    // ── Kosaraju's SCC ───────────────────────────────────────
    static int kosaraju(int n, int[][] edges) {
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
        return count;
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

    public static void main(String[] args) {
        System.out.println("Tarjan's Bridges:");
        List<int[]> bridges = findBridges(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}});
        for (int[] b : bridges) System.out.printf("  Bridge: %d-%d%n", b[0], b[1]);

        System.out.println("\nKosaraju's SCC:");
        int scc = kosaraju(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}});
        System.out.printf("  Number of SCCs: %d%n", scc); // 3
    }
}
