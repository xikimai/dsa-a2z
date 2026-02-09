package ch28.solutions;

import java.util.*;

public class Warmup04Sol {
    // Detect Cycle: return true if DAG (no cycle)
    public static boolean solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);
        int[] color = new int[n]; // 0=white, 1=gray, 2=black
        for (int i = 0; i < n; i++)
            if (color[i] == 0 && hasCycle(i, adj, color)) return false;
        return true;
    }

    private static boolean hasCycle(int u, List<List<Integer>> adj, int[] color) {
        color[u] = 1;
        for (int v : adj.get(u)) {
            if (color[v] == 1) return true;
            if (color[v] == 0 && hasCycle(v, adj, color)) return true;
        }
        color[u] = 2;
        return false;
    }
}
