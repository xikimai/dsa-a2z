package ch09.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Floor and Ceil
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Use lower bound to find ceil position, then derive floor.
 *           Floor = largest element <= target (look at position before lower bound).
 *           Ceil = smallest element >= target (the lower bound itself).
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice03Sol {

    public static int[] solve(int[] arr, int target) {
        int n = arr.length;
        // Find lower bound: first index where arr[i] >= target
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        int lb = lo;

        // Ceil: if lb < n, arr[lb] >= target, so ceil = arr[lb]; else -1
        int ceil = (lb < n) ? arr[lb] : -1;

        // Floor: if arr[lb] == target, floor = target
        //        else if lb > 0, floor = arr[lb - 1]
        //        else -1 (all elements > target)
        int floor;
        if (lb < n && arr[lb] == target) {
            floor = target;
        } else if (lb > 0) {
            floor = arr[lb - 1];
        } else {
            floor = -1;
        }

        return new int[]{floor, ceil};
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
