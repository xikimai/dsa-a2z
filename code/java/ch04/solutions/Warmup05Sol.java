package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 05: Double List
 * =====================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Iterate through the array and multiply each element by 2 in place.
 * Since arrays in Java are passed by reference (the reference is copied),
 * modifying elements inside the function changes the original array.
 *
 * TIME COMPLEXITY:  O(n) where n is the array length
 * SPACE COMPLEXITY: O(1) — modifies in place, no new array
 */
public class Warmup05Sol {

    public static int[] solve(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            nums[i] *= 2;
        }
        return nums;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }
        int[] result = solve(nums);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
