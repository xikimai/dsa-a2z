package ch14.practice;

import java.util.*;

/**
 * Challenge 1: 2D Prefix Sum and Range Query
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Build 2D prefix sum, answer rectangle queries [r1,c1,r2,c2].
 *
 * EXAMPLES:
 *   matrix = [[1,2,3],[4,5,6],[7,8,9]]
 *   queries = [[0,0,2,2],[1,1,2,2],[0,0,0,0]]
 *   -> [45, 28, 1]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01TwoDPrefixSum {
    public static long[] solve(int[][] matrix, int[][] queries) {
        // TODO: Replace this with your solution
        return new long[queries.length];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] dims = sc.nextLine().split(" ");
        int rows = Integer.parseInt(dims[0]), cols = Integer.parseInt(dims[1]);
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            String[] parts = sc.nextLine().split(" ");
            for (int j = 0; j < cols; j++) matrix[i][j] = Integer.parseInt(parts[j]);
        }
        int q = Integer.parseInt(sc.nextLine().trim());
        int[][] queries = new int[q][4];
        for (int i = 0; i < q; i++) {
            String[] parts = sc.nextLine().split(" ");
            for (int j = 0; j < 4; j++) queries[i][j] = Integer.parseInt(parts[j]);
        }
        System.out.println(Arrays.toString(solve(matrix, queries)));
        sc.close();
    }
}
