package ch19.practice;

import java.util.*;

/**
 * Practice 4: Clone Graph
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Deep clone an adjacency list (list of lists of ints).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04CloneGraph {
    public static List<List<Integer>> solve(List<List<Integer>> adj) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int k = sc.nextInt();
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < k; j++) row.add(sc.nextInt());
            adj.add(row);
        }
        List<List<Integer>> clone = solve(adj);
        for (int i = 0; i < clone.size(); i++) System.out.println(i + ": " + clone.get(i));
        sc.close();
    }
}
