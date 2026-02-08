package ch20.practice;

import java.util.*;

/**
 * Challenge 3: Making a Large Island
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Flip at most one 0 to 1. Return largest island size.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03MakingLargeIsland {
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
