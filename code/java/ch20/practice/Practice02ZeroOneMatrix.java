package ch20.practice;

import java.util.*;

/**
 * Practice 2: 01 Matrix
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Given a binary matrix, return distance of each cell to nearest 0.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02ZeroOneMatrix {
    public static int[][] solve(int[][] mat) {
        // TODO: Replace this with your solution
        return mat;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        int[][] mat = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                mat[i][j] = scan.nextInt();
        int[][] result = solve(mat);
        for (int[] row : result)
            System.out.println(Arrays.toString(row));
        scan.close();
    }
}
