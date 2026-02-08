package ch20.practice;

import java.util.*;

/**
 * Practice 1: Rotten Oranges
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Grid of 0 (empty), 1 (fresh), 2 (rotten). Each minute rotten oranges
 *          rot adjacent fresh ones. Return minutes to rot all, or -1.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01RottenOranges {
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
