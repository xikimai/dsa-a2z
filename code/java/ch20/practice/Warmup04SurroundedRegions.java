package ch20.practice;

import java.util.*;

/**
 * Warmup 4: Surrounded Regions
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Given an m x n board of 'X' and 'O', capture surrounded O regions.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04SurroundedRegions {
    public static char[][] solve(char[][] board) {
        // TODO: Replace this with your solution
        return board;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        char[][] board = new char[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                board[i][j] = scan.next().charAt(0);
        solve(board);
        for (char[] row : board)
            System.out.println(Arrays.toString(row));
        scan.close();
    }
}
