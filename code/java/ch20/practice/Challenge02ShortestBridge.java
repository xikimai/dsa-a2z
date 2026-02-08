package ch20.practice;

import java.util.*;

/**
 * Challenge 2: Shortest Bridge
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Exactly 2 islands in an n x n grid. Return minimum 0s to flip to connect them.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02ShortestBridge {
    public static int solve(int[][] grid) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = scan.nextInt();
        System.out.println(solve(grid));
        scan.close();
    }
}
