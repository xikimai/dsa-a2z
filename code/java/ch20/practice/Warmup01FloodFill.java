package ch20.practice;

import java.util.*;

/**
 * Warmup 1: Flood Fill
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Given an m x n image grid, a starting pixel (sr, sc), and a new color,
 *          flood fill all connected same-color pixels starting from (sr, sc).
 *
 * EXAMPLES:
 *   solve([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) -> [[2,2,2],[2,2,0],[2,0,1]]
 *   solve([[0,0,0],[0,0,0]], 0, 0, 0) -> [[0,0,0],[0,0,0]]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01FloodFill {
    public static int[][] solve(int[][] image, int sr, int sc, int color) {
        // TODO: Replace this with your solution
        return image;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        int sr = scan.nextInt(), sc = scan.nextInt(), color = scan.nextInt();
        int[][] image = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                image[i][j] = scan.nextInt();
        int[][] result = solve(image, sr, sc, color);
        for (int[] row : result)
            System.out.println(Arrays.toString(row));
        scan.close();
    }
}
