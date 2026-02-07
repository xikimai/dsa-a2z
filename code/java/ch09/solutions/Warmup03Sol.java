package ch09.solutions;

import java.util.*;

/**
 * Solution for Warmup 03: First Occurrence
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Binary search but when we find the target, record the
 *           index and keep searching LEFT (hi = mid - 1) to find
 *           an earlier occurrence.
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup03Sol {

    public static int solve(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        int result = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) {
                result = mid;
                hi = mid - 1;  // keep searching left
            } else if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return result;
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
