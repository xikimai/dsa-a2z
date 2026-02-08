package ch16.practice;

import java.util.*;

/**
 * Practice 3: Search in 2D Matrix
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Matrix where rows are sorted and first element of each row
 *          is greater than last element of previous row.
 *          Return [row, col] of target, or [-1, -1].
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03Search2dMatrix {
    public static int[] solve(int[][] matrix, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt(), cols = sc.nextInt();
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                matrix[i][j] = sc.nextInt();
        int target = sc.nextInt();
        System.out.println(Arrays.toString(solve(matrix, target)));
        sc.close();
    }
}
