package ch17.practice;

import java.util.*;

/**
 * Practice 2: Merge K Sorted Arrays
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Merge K sorted arrays into one sorted array.
 * EXAMPLES:
 *   solve([[1,4,7],[2,5,8],[3,6,9]]) -> [1,2,3,4,5,6,7,8,9]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02MergeKSorted {
    public static List<Integer> solve(int[][] arrays) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int[][] arrays = new int[k][];
        for (int i = 0; i < k; i++) {
            int n = sc.nextInt();
            arrays[i] = new int[n];
            for (int j = 0; j < n; j++) arrays[i][j] = sc.nextInt();
        }
        System.out.println(solve(arrays));
        sc.close();
    }
}
