package ch10.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Recursive Binary Search
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Standard binary search implemented recursively.
 *           Helper takes lo and hi bounds. Compare mid with target,
 *           recurse on appropriate half.
 *
 * TIME COMPLEXITY:  O(log n)
 * SPACE COMPLEXITY: O(log n) — call stack depth
 */
public class Practice04Sol {

    public static int solve(int[] arr, int target) {
        return helper(arr, target, 0, arr.length - 1);
    }

    private static int helper(int[] arr, int target, int lo, int hi) {
        if (lo > hi) return -1;
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) return helper(arr, target, mid + 1, hi);
        return helper(arr, target, lo, mid - 1);
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
