package ch20.practice;

import java.util.*;

/**
 * Warmup 2: Number of Islands
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Given an m x n grid of 0s and 1s, count the number of islands
 *          (connected components of 1s, 4-directional).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02NumberOfIslands {
    public static int solve(int[][] grid) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        int[][] grid = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                grid[i][j] = scan.nextInt();
        System.out.println(solve(grid));
        scan.close();
    }
}
