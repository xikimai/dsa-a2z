package ch28.learn;

import java.util.*;

/**
 * Example 01: Kahn's Algorithm Demo — BFS Topological Sort
 * =========================================================
 * Chapter 28: Topological Sort — Ordering Dependencies
 *
 * Demonstrates Kahn's Algorithm step-by-step.
 */
public class Example01KahnsDemo {

    static List<Integer> kahnsTopoSort(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            inDegree[e[1]]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            if (inDegree[i] == 0) queue.add(i);

        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            int u = queue.poll();
            result.add(u);
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) queue.add(v);
            }
        }
        return result.size() == n ? result : new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println("Kahn's Algorithm: BFS Topological Sort");
        System.out.println("=======================================");

        int[][] edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
        List<Integer> result = kahnsTopoSort(6, edges);
        System.out.println("DAG result: " + result);

        int[][] cycleEdges = {{0,1},{1,2},{2,0}};
        List<Integer> cycleResult = kahnsTopoSort(3, cycleEdges);
        System.out.println("Cycle result: " + cycleResult + " (empty = cycle detected)");
    }
}
