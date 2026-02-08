package ch19.learn;

import java.util.*;

/**
 * Example 01: Graph Representations
 * ===================================
 * Chapter 19: Graphs I — Exploring Networks
 *
 * Demonstrates three ways to represent a graph:
 *   Part 1: Adjacency List
 *   Part 2: Adjacency Matrix
 *   Part 3: Comparison and queries
 */
public class Example01GraphRepresentations {

    public static void main(String[] args) {

        // Graph:
        //   0 --- 1
        //   |     |
        //   2 --- 3
        //         |
        //         4
        int n = 5;
        int[][] edges = {{0,1}, {0,2}, {1,3}, {2,3}, {3,4}};

        // ── Part 1: Adjacency List ─────────────────────────
        System.out.println("=== Part 1: Adjacency List ===");
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        for (int i = 0; i < n; i++) {
            System.out.println("  " + i + ": " + adj.get(i));
        }
        System.out.println("  Space: O(V + 2E) = O(" + (n + 2 * edges.length) + ")");

        // ── Part 2: Adjacency Matrix ───────────────────────
        System.out.println("\n=== Part 2: Adjacency Matrix ===");
        int[][] matrix = new int[n][n];
        for (int[] e : edges) {
            matrix[e[0]][e[1]] = 1;
            matrix[e[1]][e[0]] = 1;
        }
        System.out.print("     ");
        for (int i = 0; i < n; i++) System.out.print(i + "  ");
        System.out.println();
        for (int i = 0; i < n; i++) {
            System.out.print("  " + i + ": ");
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + "  ");
            }
            System.out.println();
        }
        System.out.println("  Space: O(V^2) = O(" + (n * n) + ")");

        // ── Part 3: Queries ────────────────────────────────
        System.out.println("\n=== Part 3: Queries ===");
        System.out.println("  Neighbors of node 3 (adj list): " + adj.get(3));
        System.out.println("  Edge between 0 and 3? (matrix): " + (matrix[0][3] == 1));
        System.out.println("  Degree of node 3: " + adj.get(3).size());
    }
}
