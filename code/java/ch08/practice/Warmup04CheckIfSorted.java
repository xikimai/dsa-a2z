package ch08.practice;

import java.util.*;

/**
 * Warmup 04: Check If Sorted
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array of integers, return true if the array is
 *          sorted in non-decreasing order, false otherwise.
 *          An empty array and a single-element array are considered sorted.
 *
 * EXAMPLES:
 *   solve([1, 2, 3, 4, 5]) = true
 *   solve([1, 3, 2, 4, 5]) = false
 *   solve([])               = true
 *   solve([7])              = true
 *   solve([1, 1, 1])        = true
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^5
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04CheckIfSorted {
    public static boolean solve(int[] arr) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            String[] parts = line.split("\\s+");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            System.out.println(solve(arr));
        }
        sc.close();
    }
}
