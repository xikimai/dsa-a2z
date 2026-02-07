package ch09.practice;

import java.util.*;

/**
 * Warmup 01: Linear Search
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: Given an array of integers and a target value, return the
 *          index of the FIRST occurrence of the target, or -1 if not found.
 *
 * ALGORITHM: Scan left to right, checking each element.
 *
 * EXAMPLES:
 *   solve(new int[]{1,3,5,7,9}, 5) = 2
 *   solve(new int[]{1,3,5,7,9}, 4) = -1
 *   solve(new int[]{2,2,2,2}, 2)   = 0
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01LinearSearch {
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
