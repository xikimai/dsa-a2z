package ch09.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Search in Rotated Sorted Array
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Modified binary search. At each step, one half is always
 *           sorted. Check if the target lies in the sorted half.
 *           If yes, search there. Otherwise, search the other half.
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice04Sol {

    public static int solve(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return mid;

            // Left half is sorted
            if (arr[lo] <= arr[mid]) {
                if (arr[lo] <= target && target < arr[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }
            // Right half is sorted
            else {
                if (arr[mid] < target && target <= arr[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
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
