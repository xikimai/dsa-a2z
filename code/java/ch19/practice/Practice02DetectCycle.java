package ch19.practice;

import java.util.*;

/**
 * Practice 2: Detect Cycle in Undirected Graph
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return true if the undirected graph contains a cycle.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02DetectCycle {
    public static boolean solve(int n, int[][] edges) {
        // TODO: Replace this with your solution
        return false;
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
