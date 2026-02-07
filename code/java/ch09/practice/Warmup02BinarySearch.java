package ch09.practice;

import java.util.*;

/**
 * Warmup 02: Binary Search
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a SORTED array of integers and a target value, return
 *          the index of the target using binary search, or -1 if not found.
 *
 * ALGORITHM: Classic binary search — compare middle element with target,
 *            then search the appropriate half.
 *
 * EXAMPLES:
 *   solve(new int[]{1,3,5,7,9,11}, 7)  = 3
 *   solve(new int[]{1,3,5,7,9,11}, 4)  = -1
 *   solve(new int[]{2,4,6,8,10}, 2)    = 0
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted ascending
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 *               Use mid = lo + (hi - lo) / 2 for overflow safety.
 */
public class Warmup02BinarySearch {
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
