package ch19.practice;

import java.util.*;

/**
 * Practice 5: All Paths from Source to Target
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find all paths from node 0 to node n-1 in a DAG. Return sorted.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05AllPaths {
    public static List<List<Integer>> solve(int n, int[][] edges) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        List<List<Integer>> paths = solve(n, edges);
        for (List<Integer> path : paths) System.out.println(path);
        sc.close();
    }
}
