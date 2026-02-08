package ch16.practice;

import java.util.*;

/**
 * Practice 4: Row with Maximum 1s
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Binary matrix where each row is sorted (0s then 1s).
 *          Return index of the row with the most 1s, or -1 if all zeros.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04RowMaxOnes {
    public static int solve(int[][] matrix) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt(), cols = sc.nextInt();
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                matrix[i][j] = sc.nextInt();
        System.out.println(solve(matrix));
        sc.close();
    }
}
