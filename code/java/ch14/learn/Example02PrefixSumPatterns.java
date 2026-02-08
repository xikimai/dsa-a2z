package ch14.learn;

import java.util.*;

/**
 * Example 02: Prefix Sum Patterns
 * ================================
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * Demonstrates:
 *   Part 1 — 2D prefix sum construction and rectangle queries
 *   Part 2 — Kadane's algorithm step-by-step trace
 *   Part 3 — Prefix sum + hash map for subarray sum equals K
 */
public class Example02PrefixSumPatterns {

    public static void main(String[] args) {
        // ── Part 1: 2D Prefix Sums ──
        System.out.println("=== Part 1: 2D Prefix Sums ===");
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int rows = matrix.length, cols = matrix[0].length;

        long[][] prefix = new long[rows + 1][cols + 1];
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1]
                             - prefix[i-1][j-1] + matrix[i-1][j-1];
            }
        }

        System.out.println("  Matrix:");
        for (int[] row : matrix) System.out.println("    " + Arrays.toString(row));
        System.out.println("  2D Prefix:");
        for (long[] row : prefix) System.out.println("    " + Arrays.toString(row));

        // Query (1,1) to (2,2)
        long sum = prefix[3][3] - prefix[1][3] - prefix[3][1] + prefix[1][1];
        System.out.println("  rect_sum(1,1 to 2,2) = " + sum + "  (verify: 5+6+8+9=28)\n");

        // ── Part 2: Kadane's Trace ──
        System.out.println("=== Part 2: Kadane's Algorithm Trace ===");
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("  Input: " + Arrays.toString(arr));

        long currentSum = arr[0];
        long maxSum = arr[0];
        System.out.println("  i=0: current=" + currentSum + " max=" + maxSum);

        for (int i = 1; i < arr.length; i++) {
            String action = (currentSum + arr[i] >= arr[i]) ? "extend" : "RESTART";
            currentSum = Math.max(currentSum + arr[i], arr[i]);
            maxSum = Math.max(maxSum, currentSum);
            System.out.println("  i=" + i + ": arr=" + arr[i] + " current=" + currentSum
                + " max=" + maxSum + " (" + action + ")");
        }
        System.out.println("  Answer: " + maxSum + "\n");

        // ── Part 3: Prefix Sum + Hash Map ──
        System.out.println("=== Part 3: Prefix Sum + Hash Map ===");
        int[] arr2 = {1, 2, 3, -2, 5};
        int k = 3;
        System.out.println("  arr=" + Arrays.toString(arr2) + ", k=" + k);

        Map<Long, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0L, 1);
        long runSum = 0;
        int count = 0;

        for (int i = 0; i < arr2.length; i++) {
            runSum += arr2[i];
            long complement = runSum - k;
            int found = prefixCount.getOrDefault(complement, 0);
            count += found;
            System.out.println("  i=" + i + " sum=" + runSum + " need=" + complement
                + (found > 0 ? " FOUND!" : "") + " count=" + count);
            prefixCount.put(runSum, prefixCount.getOrDefault(runSum, 0) + 1);
        }
        System.out.println("  Total subarrays with sum=" + k + ": " + count);
    }
}
