package ch19.practice;

import java.util.*;

/**
 * Challenge 1: Number of Provinces
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Given an adjacency matrix, count the number of provinces
 *          (connected components).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01NumProvinces {
    public static int solve(int[][] isConnected) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] isConnected = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) isConnected[i][j] = sc.nextInt();
        System.out.println(solve(isConnected));
        sc.close();
    }
}
