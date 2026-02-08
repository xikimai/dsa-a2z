package ch10.practice;

import java.util.*;

/**
 * Practice 03: Count Occurrences (Recursive)
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an array of integers and a target value, return how many
 *          times the target appears in the array. Use recursion.
 *
 * ALGORITHM: Check the first element, then recurse on the rest.
 *
 * EXAMPLES:
 *   solve(new int[]{1,2,3,2,4,2}, 2) = 3
 *   solve(new int[]{1,2,3}, 4)       = 0
 *   solve(new int[]{}, 1)            = 0
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03CountOccurrences {
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
