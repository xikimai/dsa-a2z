package ch20.practice;

import java.util.*;

/**
 * Challenge 4: Swim in Rising Water
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Return minimum time to swim from (0,0) to (n-1,n-1).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04SwimInRisingWater {
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
