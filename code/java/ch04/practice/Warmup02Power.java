package ch04.practice;

import java.util.Scanner;

/**
 * Warmup 02: Power
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that computes base^exponent using a loop.
 * Do NOT use Math.pow — implement it yourself!
 *
 * INPUT FORMAT
 * ------------
 * Two integers on one line: base and exponent, separated by a space.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the result of base^exponent.
 *
 * CONSTRAINTS
 * -----------
 * - base can be any integer
 * - exponent >= 0
 * - Result fits in a long
 *
 * EXAMPLES
 * --------
 * Input:  2 10
 * Output: 1024
 *
 * Input:  5 0
 * Output: 1
 *
 * Input:  3 4
 * Output: 81
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0L;" in the solve() method with your solution.
 * Use a loop, not Math.pow.
 * The main method handles input/output -- don't change it.
 */
public class Warmup02Power {

    /**
     * Compute base raised to the exponent using a loop.
     *
     * @param base     the base number
     * @param exponent the exponent (non-negative)
     * @return base^exponent
     */
    public static long solve(int base, int exponent) {
        // TODO: Replace this with your solution
        return 0L;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int base = sc.nextInt();
        int exponent = sc.nextInt();
        System.out.println(solve(base, exponent));
        sc.close();
    }
}
