package ch19.practice;

import java.util.*;

/**
 * Practice 3: Bipartite Check
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return true if the graph is bipartite (2-colorable).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03BipartiteCheck {
    public static boolean solve(int n, int[][] edges) {
        // TODO: Replace this with your solution
        return true;
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
