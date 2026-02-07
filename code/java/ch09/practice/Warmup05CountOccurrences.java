package ch09.practice;

import java.util.*;

/**
 * Warmup 05: Count Occurrences
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given a SORTED array of integers and a target, count how
 *          many times the target appears in the array.
 *
 * ALGORITHM: Use first occurrence + last occurrence to compute count
 *            in O(log n) time. Count = last - first + 1 (if found).
 *
 * EXAMPLES:
 *   solve(new int[]{1,2,2,2,3,4}, 2) = 3
 *   solve(new int[]{1,1,1,1,1}, 1)   = 5
 *   solve(new int[]{1,3,5,7}, 4)     = 0
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted ascending
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05CountOccurrences {
    public static int solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return 0;
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
