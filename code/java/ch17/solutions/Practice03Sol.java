package ch17.solutions;

import java.util.*;

/**
 * Solution for Practice 3: Kth Smallest Element in a Sorted Matrix
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Min-heap pushing first element of each row, pop k times.
 * TIME:  O(k log n)
 * SPACE: O(n)
 */
public class Practice03Sol {
    public static int solve(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> Integer.compare(a[0], b[0])
        );
        for (int r = 0; r < n; r++) {
            pq.add(new int[]{matrix[r][0], r, 0});
        }
        int val = 0;
        for (int i = 0; i < k; i++) {
            int[] top = pq.poll();
            val = top[0];
            int r = top[1], c = top[2];
            if (c + 1 < matrix[r].length) {
                pq.add(new int[]{matrix[r][c + 1], r, c + 1});
            }
        }
        return val;
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
