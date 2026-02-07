package ch09.practice;

import java.util.*;

/**
 * Practice 05: Find Minimum in Rotated Sorted Array
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a rotated sorted array (no duplicates), find the
 *          minimum element value.
 *
 * ALGORITHM: Binary search — compare mid with hi to decide which
 *            half contains the minimum.
 *
 * EXAMPLES:
 *   solve(new int[]{3,4,5,1,2})       = 1
 *   solve(new int[]{4,5,6,7,0,1,2})   = 0
 *   solve(new int[]{1,2,3,4,5})       = 1
 *
 * CONSTRAINTS: 1 <= arr.length <= 10^5, no duplicates
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05MinInRotated {
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
