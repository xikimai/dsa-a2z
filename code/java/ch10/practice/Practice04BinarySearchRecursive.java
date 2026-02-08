package ch10.practice;

import java.util.*;

/**
 * Practice 04: Recursive Binary Search
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a sorted array of integers and a target, return the index
 *          of the target using recursive binary search. Return -1 if not found.
 *
 * ALGORITHM: Compare target with mid element. Recurse on left or right half.
 *
 * EXAMPLES:
 *   solve(new int[]{1,3,5,7,9}, 5) = 2
 *   solve(new int[]{1,3,5,7,9}, 4) = -1
 *   solve(new int[]{}, 1)          = -1
 *
 * CONSTRAINTS: 0 <= arr.length <= 10^5, array is sorted in ascending order
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04BinarySearchRecursive {
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
