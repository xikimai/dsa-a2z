package ch19.practice;

import java.util.*;

/**
 * Warmup 3: DFS Traversal
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return DFS traversal order from source (visit smallest neighbor first).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03DfsTraversal {
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
