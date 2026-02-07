package ch09.solutions;

import java.util.*;

/**
 * Solution for Warmup 01: Linear Search
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Scan the array left to right. Return the first index
 *           where the element matches the target.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup01Sol {

    public static int solve(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
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
