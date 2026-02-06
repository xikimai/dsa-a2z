package ch04.practice;

import java.util.Scanner;

/**
 * Warmup 05: Double List
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that takes an integer array and doubles every element
 * in place, then returns the modified array.
 *
 * This demonstrates how arrays are passed by reference in Java — changes
 * to the array inside the function affect the original array.
 *
 * INPUT FORMAT
 * ------------
 * First line: n (number of elements)
 * Second line: n space-separated integers
 *
 * OUTPUT FORMAT
 * -------------
 * Print the doubled array, elements separated by spaces.
 *
 * CONSTRAINTS
 * -----------
 * - 1 <= n <= 100
 * - -1000 <= each element <= 1000
 *
 * EXAMPLES
 * --------
 * Input:  5
 *         1 2 3 4 5
 * Output: 2 4 6 8 10
 *
 * Input:  3
 *         -1 0 7
 * Output: -2 0 14
 *
 * INSTRUCTIONS
 * ------------
 * Modify the array in place (change each element to element * 2).
 * Return the same array.
 * The main method handles input/output -- don't change it.
 */
public class Warmup05DoubleList {

    /**
     * Double every element of the array in place.
     *
     * @param nums the array to modify
     * @return the same array with doubled values
     */
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
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
