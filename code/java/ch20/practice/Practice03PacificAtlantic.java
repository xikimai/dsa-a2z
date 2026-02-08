package ch20.practice;

import java.util.*;

/**
 * Practice 3: Pacific Atlantic Water Flow
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Given heights grid, return cells that can reach both Pacific and Atlantic.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03PacificAtlantic {
    public static List<int[]> solve(int[][] heights) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        int[][] heights = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                heights[i][j] = scan.nextInt();
        List<int[]> result = solve(heights);
        for (int[] cell : result)
            System.out.println(cell[0] + " " + cell[1]);
        scan.close();
    }
}
