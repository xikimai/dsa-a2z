package ch09.practice;

import java.util.*;

/**
 * Warmup 04: Last Occurrence
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a SORTED array of integers and a target, return the
 *          index of the LAST (rightmost) occurrence of the target,
 *          or -1 if not found.
 *
 * ALGORITHM: Modified binary search — when you find the target, don't
 *            stop! Keep searching RIGHT for a later occurrence.
 *
 * EXAMPLES:
 *   solve(new int[]{1,2,2,2,3,4}, 2) = 3
 *   solve(new int[]{1,1,1,1,1}, 1)   = 4
 *   solve(new int[]{1,3,5,7}, 4)     = -1
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted ascending
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04LastOccurrence {
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
