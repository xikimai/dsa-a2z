package ch09.practice;

import java.util.*;

/**
 * Practice 04: Search in Rotated Sorted Array
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a rotated sorted array (no duplicates) and a target,
 *          return the index of the target, or -1 if not found.
 *
 * ALGORITHM: Modified binary search — at each step, one half is always
 *            sorted. Check if the target falls in the sorted half.
 *
 * EXAMPLES:
 *   solve(new int[]{4,5,6,7,0,1,2}, 0) = 4
 *   solve(new int[]{4,5,6,7,0,1,2}, 3) = -1
 *   solve(new int[]{1}, 1)              = 0
 *
 * CONSTRAINTS: 1 <= arr.length <= 10^5, no duplicates
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04SearchRotated {
    public static int solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return -1;
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
