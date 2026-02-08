package ch19.practice;

import java.util.*;

/**
 * Warmup 4: Count Connected Components
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Count the number of connected components in an undirected graph.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04CountComponents {
    public static int solve(int n, int[][] edges) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        System.out.println(solve(n, edges));
        sc.close();
    }
}
