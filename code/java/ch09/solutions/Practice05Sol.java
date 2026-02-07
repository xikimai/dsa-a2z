package ch09.solutions;

import java.util.*;

/**
 * Solution for Practice 05: Find Minimum in Rotated Sorted Array
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Binary search comparing mid with hi. If arr[mid] > arr[hi],
 *           the minimum is in the right half. Otherwise, it's in the
 *           left half (including mid).
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice05Sol {

    public static int solve(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > arr[hi]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return arr[lo];
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
