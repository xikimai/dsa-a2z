package ch09.practice;

import java.util.*;

/**
 * Challenge 03: Search in Rotated Sorted Array II (with duplicates)
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a rotated sorted array that MAY CONTAIN DUPLICATES
 *          and a target, return true if the target exists, false otherwise.
 *
 * ALGORITHM: Modified binary search for rotated arrays. When duplicates
 *            make it impossible to determine which half is sorted
 *            (arr[lo]==arr[mid]==arr[hi]), shrink from both ends.
 *
 * EXAMPLES:
 *   solve(new int[]{2,5,6,0,0,1,2}, 0)  = true
 *   solve(new int[]{2,5,6,0,0,1,2}, 3)  = false
 *   solve(new int[]{1,0,1,1,1}, 0)      = true
 *
 * CONSTRAINTS: 1 <= arr.length <= 10^5, may contain duplicates
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03RotatedSearchII {
    public static boolean solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return false;
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
