package ch27.learn;

import java.util.*;

/**
 * Example 02: Bellman-Ford Algorithm — Handling Negative Weights
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
public class Example02BellmanFordDemo {

    static int[] bellmanFord(int n, int[][] edges, int src) {
        int INF = (int) 1e9;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;

        for (int round = 1; round < n; round++) {
            boolean updated = false;
            for (int[] e : edges) {
                if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]]) {
                    System.out.println("  Round " + round + ": Relax " + e[0] + " -> " + e[1] + ": " + dist[e[1]] + " -> " + (dist[e[0]] + e[2]));
                    dist[e[1]] = dist[e[0]] + e[2];
                    updated = true;
                }
            }
            if (!updated) {
                System.out.println("  Round " + round + ": No updates — early stop!");
                break;
            }
        }

        // Negative cycle check
        for (int[] e : edges) {
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]]) {
                System.out.println("  NEGATIVE CYCLE DETECTED!");
                return null;
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        int[][] edges = {{0,1,-1},{0,2,4},{1,2,3},{1,3,2},{1,4,2},{3,2,5},{3,1,1},{4,3,-3}};
        System.out.println("Bellman-Ford Algorithm Demo");
        System.out.println("==========================");
        int[] dist = bellmanFord(5, edges, 0);
        if (dist != null) System.out.println("Distances: " + Arrays.toString(dist));
    }
}
