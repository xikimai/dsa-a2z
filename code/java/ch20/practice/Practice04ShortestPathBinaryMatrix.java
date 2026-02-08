package ch20.practice;

import java.util.*;

/**
 * Practice 4: Shortest Path in Binary Matrix
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Find shortest clear path from (0,0) to (n-1,n-1) in a binary grid.
 *          Movement is 8-directional. Path length = number of cells visited.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04ShortestPathBinaryMatrix {
    public static int solve(int[][] grid) {
        // TODO: Replace this with your solution
        return -1;
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
