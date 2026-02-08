package ch10.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Count Occurrences (Recursive)
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Use a helper with an index parameter.
 *           At each index, add 1 if element matches target, then recurse.
 *           Base case: index == array length.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Practice03Sol {

    public static int solve(int[] arr, int target) {
        return helper(arr, target, 0);
    }

    private static int helper(int[] arr, int target, int idx) {
        if (idx == arr.length) return 0;
        int count = (arr[idx] == target) ? 1 : 0;
        return count + helper(arr, target, idx + 1);
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
