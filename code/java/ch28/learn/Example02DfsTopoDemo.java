package ch28.learn;

import java.util.*;

/**
 * Example 02: DFS-Based Topological Sort with Cycle Detection
 * =============================================================
 * Chapter 28: Topological Sort — Ordering Dependencies
 *
 * Demonstrates DFS topo sort with three-color cycle detection.
 */
public class Example02DfsTopoDemo {

    static boolean hasCycle;

    static void dfs(int u, List<List<Integer>> adj, int[] color, Deque<Integer> stack) {
        if (hasCycle) return;
        color[u] = 1; // gray
        for (int v : adj.get(u)) {
            if (color[v] == 1) { hasCycle = true; return; }
            if (color[v] == 0) dfs(v, adj, color, stack);
        }
        color[u] = 2; // black
        stack.push(u);
    }

    static List<Integer> dfsTopoSort(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);

        int[] color = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        hasCycle = false;

        for (int i = 0; i < n; i++)
            if (color[i] == 0) dfs(i, adj, color, stack);

        if (hasCycle) return new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        while (!stack.isEmpty()) result.add(stack.pop());
        return result;
    }

    public static void main(String[] args) {
        System.out.println("DFS Topological Sort: Three-Color Cycle Detection");
        System.out.println("==================================================");

        int[][] edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
        System.out.println("DAG result: " + dfsTopoSort(6, edges));

        int[][] cycleEdges = {{0,1},{1,2},{2,0}};
        System.out.println("Cycle result: " + dfsTopoSort(3, cycleEdges));
    }
}
