package ch29.learn;

import java.util.*;

/**
 * Example 02: MST Demo — Kruskal's and Prim's Side by Side
 * ==========================================================
 * Chapter 29: Union-Find & Minimum Spanning Trees
 *
 * Demonstrates both MST algorithms on the same graph.
 */
public class Example02MstDemo {

    // Union-Find for Kruskal's
    static int[] parent, rank;

    static void init(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    static boolean union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
        return true;
    }

    static int kruskal(int n, int[][] edges) {
        init(n);
        Arrays.sort(edges, (a, b) -> a[2] - b[2]);
        int total = 0;
        for (int[] e : edges)
            if (union(e[0], e[1])) total += e[2];
        return total;
    }

    @SuppressWarnings("unchecked")
    static int prim(int n, int[][] edges) {
        List<int[]>[] adj = new List[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[2], e[1]});
            adj[e[1]].add(new int[]{e[2], e[0]});
        }
        boolean[] vis = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});
        int total = 0, count = 0;
        while (!pq.isEmpty() && count < n) {
            int[] top = pq.poll();
            if (vis[top[1]]) continue;
            vis[top[1]] = true;
            total += top[0];
            count++;
            for (int[] nb : adj[top[1]])
                if (!vis[nb[1]]) pq.offer(nb);
        }
        return total;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] edges = {
            {0,1,4}, {0,2,8}, {1,2,2}, {1,3,6}, {2,3,3}, {2,4,9}, {3,4,5}
        };
        System.out.println("MST Demo");
        System.out.printf("  Kruskal's: %d%n", kruskal(n, edges.clone()));
        System.out.printf("  Prim's:    %d%n", prim(n, edges));
    }
}
