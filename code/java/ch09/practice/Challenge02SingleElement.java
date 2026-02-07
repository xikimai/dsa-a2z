package ch09.practice;

import java.util.*;

/**
 * Challenge 02: Single Element in Sorted Array
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: In a sorted array where every element appears exactly twice
 *          except for one element that appears once, find that single
 *          element in O(log n) time.
 *
 * ALGORITHM: Binary search using the index parity trick — before the
 *            single element, pairs start at even indices; after it,
 *            pairs start at odd indices.
 *
 * EXAMPLES:
 *   solve(new int[]{1,1,2,3,3,4,4,8,8}) = 2
 *   solve(new int[]{3,3,7,7,10,11,11})  = 10
 *   solve(new int[]{1})                  = 1
 *
 * CONSTRAINTS: 1 <= arr.length <= 10^5, arr.length is odd
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02SingleElement {
    public static int solve(int[] arr) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr;
        if (line.isEmpty()) {
            arr = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
        }
        System.out.println(solve(arr));
        sc.close();
    }
}
