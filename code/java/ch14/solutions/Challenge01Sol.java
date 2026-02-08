package ch14.solutions;

import java.util.*;

public class Challenge01Sol {
    public static long[] solve(int[][] matrix, int[][] queries) {
        if (matrix.length == 0 || matrix[0].length == 0) return new long[queries.length];
        int rows = matrix.length, cols = matrix[0].length;
        long[][] prefix = new long[rows + 1][cols + 1];
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1]
                             - prefix[i-1][j-1] + matrix[i-1][j-1];
            }
        }
        long[] result = new long[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int r1 = queries[q][0], c1 = queries[q][1];
            int r2 = queries[q][2], c2 = queries[q][3];
            result[q] = prefix[r2+1][c2+1] - prefix[r1][c2+1]
                      - prefix[r2+1][c1] + prefix[r1][c1];
        }
        return result;
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
