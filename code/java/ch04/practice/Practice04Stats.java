package ch04.practice;

import java.util.Scanner;

/**
 * Practice 04: Array Statistics
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that returns the [min, max, average] of an integer
 * array using helper functions findMin(), findMax(), and findAverage().
 *
 * Do NOT use built-in Math.min, Math.max, or stream methods.
 * Implement the logic yourself!
 *
 * INPUT FORMAT
 * ------------
 * First line: n (number of elements)
 * Second line: n space-separated integers
 *
 * OUTPUT FORMAT
 * -------------
 * Print three values on one line: min max average
 * Average is rounded to 2 decimal places.
 *
 * CONSTRAINTS
 * -----------
 * - 1 <= n <= 1000
 * - -10^6 <= each element <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  5
 *         3 1 4 1 5
 * Output: 1 5 2.80
 *
 * Input:  3
 *         10 20 30
 * Output: 10 30 20.00
 *
 * Input:  1
 *         42
 * Output: 42 42 42.00
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement findMin(), findMax(), findAverage() helpers.
 * 2. Implement solve() that returns a double[] of {min, max, average}.
 * 3. Average is rounded: Math.round(avg * 100.0) / 100.0
 * The main method handles input/output -- don't change it.
 */
public class Practice04Stats {

    /**
     * Find the minimum value in an array.
     *
     * @param nums the array
     * @return the minimum value
     */
    public static int findMin(int[] nums) {
        // TODO: Implement (no Math.min!)
        return 0;
    }

    /**
     * Find the maximum value in an array.
     *
     * @param nums the array
     * @return the maximum value
     */
    public static int findMax(int[] nums) {
        // TODO: Implement (no Math.max!)
        return 0;
    }

    /**
     * Find the average of all values in an array.
     *
     * @param nums the array
     * @return the average, rounded to 2 decimal places
     */
    public static double findAverage(int[] nums) {
        // TODO: Implement
        return 0.0;
    }

    /**
     * Return [min, max, average] of the array.
     *
     * @param nums the array
     * @return a double[] containing {min, max, average}
     */
    public static double[] solve(int[] nums) {
        // TODO: Replace this with your solution
        return new double[0];
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
