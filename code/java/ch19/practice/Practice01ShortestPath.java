package ch19.practice;

import java.util.*;

/**
 * Practice 1: Shortest Path (Unweighted)
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find shortest distances from source to all nodes. -1 if unreachable.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01ShortestPath {
    public static int[] solve(int n, int[][] edges, int source) {
        // TODO: Replace this with your solution
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        return dist;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), source = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        System.out.println(Arrays.toString(solve(n, edges, source)));
        sc.close();
    }
}
