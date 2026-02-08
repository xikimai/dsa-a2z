package ch14.practice;

import java.util.*;

/**
 * Warmup 2: Range Sum Query
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given an array and queries [l, r], return the sum of
 *          arr[l..r] (inclusive, 0-indexed) for each query.
 *
 * EXAMPLES:
 *   solve([3,1,4,1,5,9], [[0,5],[2,4],[3,3]]) -> [23, 10, 1]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02RangeSumQuery {
    public static long[] solve(int[] arr, int[][] queries) {
        // TODO: Replace this with your solution
        return new long[queries.length];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int q = Integer.parseInt(sc.nextLine().trim());
        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            String[] parts = sc.nextLine().split(" ");
            queries[i][0] = Integer.parseInt(parts[0]);
            queries[i][1] = Integer.parseInt(parts[1]);
        }
        System.out.println(Arrays.toString(solve(arr, queries)));
        sc.close();
    }
}
