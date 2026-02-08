package ch19.practice;

import java.util.*;

/**
 * Warmup 5: Is Path Exists
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Determine if a path exists between source and dest.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05IsPathExists {
    public static boolean solve(int n, int[][] edges, int source, int dest) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), source = sc.nextInt(), dest = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        System.out.println(solve(n, edges, source, dest));
        sc.close();
    }
}
