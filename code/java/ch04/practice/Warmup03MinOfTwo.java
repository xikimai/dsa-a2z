package ch04.practice;

import java.util.Scanner;

/**
 * Warmup 03: Min of Three (using Min of Two)
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a helper function minOfTwo(a, b) that returns the smaller of two
 * integers. Then use it to write solve(a, b, c) that returns the minimum
 * of three integers.
 *
 * INPUT FORMAT
 * ------------
 * Three integers on one line, separated by spaces.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the minimum of the three numbers.
 *
 * CONSTRAINTS
 * -----------
 * Integers can be negative, zero, or positive.
 *
 * EXAMPLES
 * --------
 * Input:  3 1 2
 * Output: 1
 *
 * Input:  -5 -2 -8
 * Output: -8
 *
 * Input:  7 7 7
 * Output: 7
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement the minOfTwo() helper first.
 * 2. Then implement solve() using minOfTwo().
 * Do NOT use Math.min — write your own!
 * The main method handles input/output -- don't change it.
 */
public class Warmup03MinOfTwo {

    /**
     * Return the smaller of two integers.
     *
     * @param a first integer
     * @param b second integer
     * @return the minimum of a and b
     */
    public static int minOfTwo(int a, int b) {
        // TODO: Implement this helper
        return 0;
    }

    /**
     * Return the minimum of three integers using minOfTwo.
     *
     * @param a first integer
     * @param b second integer
     * @param c third integer
     * @return the minimum of a, b, and c
     */
    public static int solve(int a, int b, int c) {
        // TODO: Replace this with your solution (use minOfTwo!)
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.println(solve(a, b, c));
        sc.close();
    }
}
