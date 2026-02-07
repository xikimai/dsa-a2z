package ch09.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: Search in Rotated Sorted Array II (with duplicates)
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Modified binary search for rotated array with duplicates.
 *           The key difference from the no-duplicates version: when
 *           arr[lo] == arr[mid] == arr[hi], we can't determine which
 *           half is sorted, so we shrink from both ends.
 *
 * TIME COMPLEXITY:  O(log n) average, O(n) worst case (all duplicates)
 * SPACE COMPLEXITY: O(1)
 */
public class Challenge03Sol {

    public static boolean solve(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return true;

            // When we can't tell which side is sorted
            if (arr[lo] == arr[mid] && arr[mid] == arr[hi]) {
                lo++;
                hi--;
            }
            // Left half is sorted
            else if (arr[lo] <= arr[mid]) {
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
