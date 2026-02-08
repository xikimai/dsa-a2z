package ch19.practice;

import java.util.*;

/**
 * Warmup 1: Build Adjacency List
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Given n nodes and edges for an undirected graph, build the
 *          adjacency list. Each node's neighbors should be sorted.
 *
 * EXAMPLES:
 *   solve(4, {{0,1},{0,2},{1,3}}) -> [[1,2],[0,3],[0],[1]]
 *   solve(3, {})                  -> [[],[],[]]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01BuildAdjList {
    public static List<List<Integer>> solve(int n, int[][] edges) {
        // TODO: Replace this with your solution
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        return adj;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        List<List<Integer>> adj = solve(n, edges);
        for (int i = 0; i < n; i++) System.out.println(i + ": " + adj.get(i));
        sc.close();
    }
}
