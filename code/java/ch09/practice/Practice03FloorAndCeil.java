package ch09.practice;

import java.util.*;

/**
 * Practice 03: Floor and Ceil
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a SORTED array and a target, find:
 *          - Floor: largest element <= target (-1 if none)
 *          - Ceil:  smallest element >= target (-1 if none)
 *          Return as int[]{floor, ceil}.
 *
 * ALGORITHM: Use binary search to find lower bound, then derive
 *            floor and ceil from the position.
 *
 * EXAMPLES:
 *   solve(new int[]{1,3,5,7,9}, 5)  = {5, 5}
 *   solve(new int[]{1,3,5,7,9}, 4)  = {3, 5}
 *   solve(new int[]{1,3,5,7,9}, 0)  = {-1, 1}
 *   solve(new int[]{1,3,5,7,9}, 10) = {9, -1}
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted ascending
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03FloorAndCeil {
    public static int[] solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
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
        int[] result = solve(arr, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
