package ch09.solutions;

import java.util.*;

/**
 * Solution for Practice 01: Lower Bound
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Binary search to find the first index where arr[i] >= target.
 *           Start with answer = arr.length (all smaller case).
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice01Sol {

    public static int solve(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
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
