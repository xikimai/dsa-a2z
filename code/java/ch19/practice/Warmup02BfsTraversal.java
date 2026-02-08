package ch19.practice;

import java.util.*;

/**
 * Warmup 2: BFS Traversal
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return BFS traversal order from source (visit smallest neighbor first).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02BfsTraversal {
    public static List<Integer> solve(int n, int[][] edges, int source) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), source = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        System.out.println(solve(n, edges, source));
        sc.close();
    }
}
