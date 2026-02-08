package ch19.learn;

import java.util.*;

/**
 * Example 02: BFS vs DFS
 * ========================
 * Chapter 19: Graphs I — Exploring Networks
 *
 * Demonstrates:
 *   Part 1: BFS traversal step by step
 *   Part 2: DFS traversal step by step
 *   Part 3: BFS finds shortest paths, DFS does not
 */
public class Example02BfsVsDfs {

    public static void main(String[] args) {
        // Graph:
        //   0 --- 1
        //   |     |
        //   2 --- 3
        //         |
        //         4
        int n = 5;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        int[][] edges = {{0,1}, {0,2}, {1,3}, {2,3}, {3,4}};
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        // ── Part 1: BFS ───────────────────────────────────
        System.out.println("=== Part 1: BFS from node 0 ===");
        boolean[] visitedBfs = new boolean[n];
        visitedBfs[0] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        List<Integer> bfsOrder = new ArrayList<>();

        while (!queue.isEmpty()) {
            int node = queue.poll();
            bfsOrder.add(node);
            List<Integer> nbrs = new ArrayList<>(adj.get(node));
            Collections.sort(nbrs);
            for (int nb : nbrs) {
                if (!visitedBfs[nb]) {
                    visitedBfs[nb] = true;
                    queue.add(nb);
                }
            }
        }
        System.out.println("  BFS order: " + bfsOrder);

        // ── Part 2: DFS ───────────────────────────────────
        System.out.println("\n=== Part 2: DFS from node 0 ===");
        boolean[] visitedDfs = new boolean[n];
        List<Integer> dfsOrder = new ArrayList<>();
        dfs(adj, 0, visitedDfs, dfsOrder);
        System.out.println("  DFS order: " + dfsOrder);

        // ── Part 3: Shortest Paths ─────────────────────────
        System.out.println("\n=== Part 3: Shortest Paths (BFS vs DFS) ===");
        // Smaller graph: 0-1, 0-2, 1-3, 2-3
        int m = 4;
        List<List<Integer>> adj2 = new ArrayList<>();
        for (int i = 0; i < m; i++) adj2.add(new ArrayList<>());
        adj2.get(0).add(1); adj2.get(1).add(0);
        adj2.get(0).add(2); adj2.get(2).add(0);
        adj2.get(1).add(3); adj2.get(3).add(1);
        adj2.get(2).add(3); adj2.get(3).add(2);

        // BFS distances
        int[] distBfs = new int[m];
        Arrays.fill(distBfs, -1);
        distBfs[0] = 0;
        Queue<Integer> q2 = new LinkedList<>();
        q2.add(0);
        while (!q2.isEmpty()) {
            int node = q2.poll();
            for (int nb : adj2.get(node)) {
                if (distBfs[nb] == -1) {
                    distBfs[nb] = distBfs[node] + 1;
                    q2.add(nb);
                }
            }
        }
        System.out.println("  BFS distances from 0: " + Arrays.toString(distBfs));
        System.out.println("  BFS is CORRECT for shortest paths!");
        System.out.println("  DFS would give wrong distances (e.g., dist[2]=3 instead of 1)");
    }

    static void dfs(List<List<Integer>> adj, int node,
                     boolean[] visited, List<Integer> order) {
        visited[node] = true;
        order.add(node);
        List<Integer> nbrs = new ArrayList<>(adj.get(node));
        Collections.sort(nbrs);
        for (int nb : nbrs) {
            if (!visited[nb]) {
                dfs(adj, nb, visited, order);
            }
        }
    }
}
