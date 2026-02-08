package ch17.practice;

import java.util.*;

/**
 * Practice 3: Kth Smallest Element in a Sorted Matrix
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Find kth smallest element in row/col sorted matrix.
 * EXAMPLES:
 *   solve([[1,5,9],[10,11,13],[12,13,15]], 8) -> 13
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03KthSmallestMatrix {
    public static int solve(int[][] matrix, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matrix[i][j] = sc.nextInt();
        int k = sc.nextInt();
        System.out.println(solve(matrix, k));
        sc.close();
    }
}
