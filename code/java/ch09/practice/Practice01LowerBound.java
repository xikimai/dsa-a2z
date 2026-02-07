package ch09.practice;

import java.util.*;

/**
 * Practice 01: Lower Bound
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a SORTED array, find the first index where
 *          arr[i] >= target. Return arr.length if all elements
 *          are smaller than target.
 *
 * ALGORITHM: Binary search variant — narrow the range to find the
 *            insertion point for the target.
 *
 * EXAMPLES:
 *   solve(new int[]{1,3,5,7,9}, 5)  = 2  (arr[2]=5 >= 5)
 *   solve(new int[]{1,3,5,7,9}, 4)  = 2  (arr[2]=5 >= 4)
 *   solve(new int[]{1,3,5,7,9}, 10) = 5  (all smaller)
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted ascending
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01LowerBound {
    public static int solve(int[] arr, int target) {
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
        int target = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(arr, target));
        sc.close();
    }
}
