package ch27.learn;

import java.util.*;

/**
 * Example 01: Dijkstra's Algorithm — Step-by-Step Demo
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
public class Example01DijkstraDemo {

    static int[] dijkstra(int n, int[][] edges, int src) {
        int INF = (int) 1e9;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) adj[e[0]].add(new int[]{e[1], e[2]});

        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, src});

        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int d = top[0], u = top[1];
            if (d > dist[u]) continue;
            System.out.println("  Process node " + u + " (distance = " + d + ")");
            for (int[] edge : adj[u]) {
                int v = edge[0], w = edge[1];
                if (dist[u] + w < dist[v]) {
                    System.out.println("    Relax " + u + " -> " + v + ": " + dist[v] + " -> " + (dist[u] + w));
                    dist[v] = dist[u] + w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        int[][] edges = {{0,1,4},{0,2,1},{2,1,2},{1,3,5},{2,3,8},{3,4,1}};
        System.out.println("Dijkstra's Algorithm Demo");
        System.out.println("=========================");
        int[] dist = dijkstra(5, edges, 0);
        System.out.println("Distances: " + Arrays.toString(dist));
    }
}
