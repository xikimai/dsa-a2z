package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 04: Array Statistics
 * ============================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three helper functions each iterate through the array once:
 *   - findMin: track the smallest value seen so far
 *   - findMax: track the largest value seen so far
 *   - findAverage: sum all elements, divide by length, round to 2 decimals
 *
 * TIME COMPLEXITY:  O(n) — three passes through the array
 * SPACE COMPLEXITY: O(1) — only a few variables
 */
public class Practice04Sol {

    public static int findMin(int[] nums) {
        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < min) min = nums[i];
        }
        return min;
    }

    public static int findMax(int[] nums) {
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) max = nums[i];
        }
        return max;
    }

    public static double findAverage(int[] nums) {
        long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        double avg = (double) sum / nums.length;
        return Math.round(avg * 100.0) / 100.0;
    }

    public static double[] solve(int[] nums) {
        return new double[]{findMin(nums), findMax(nums), findAverage(nums)};
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
        double[] result = solve(nums);
        if (result.length == 3) {
            System.out.printf("%.0f %.0f %.2f%n", result[0], result[1], result[2]);
        }
        sc.close();
    }
}
