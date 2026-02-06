package ch01.practice;

import java.util.Scanner;

/**
 * Warmup 01: Sum of Two Numbers
 * ==============================
 * Chapter 1: The Coder's Toolkit
 *
 * PROBLEM
 * -------
 * Given two integers, print their sum.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing two space-separated integers a and b.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single integer — the sum of a and b.
 *
 * CONSTRAINTS
 * -----------
 * -10^6 <= a, b <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  1 2
 * Output: 3
 *
 * Input:  0 0
 * Output: 0
 *
 * Input:  -5 5
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * The main method handles input/output — don't change it.
 */
public class Warmup01Sum {

    /**
     * Return the sum of a and b.
     *
     * @param a the first integer
     * @param b the second integer
     * @return the sum of a and b
     */
    public static int solve(int a, int b) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println(solve(a, b));
        scanner.close();
    }
}
