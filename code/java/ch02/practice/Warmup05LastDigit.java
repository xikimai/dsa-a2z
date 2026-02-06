package ch02.practice;

import java.util.Scanner;

/**
 * Warmup 05: Last Digit
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given an integer n, return its last digit.
 * The last digit should always be non-negative (use Math.abs).
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single integer — the last digit of n.
 *
 * CONSTRAINTS
 * -----------
 * -10^9 <= n <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  1234
 * Output: 4
 *
 * Input:  -567
 * Output: 7
 *
 * Input:  0
 * Output: 0
 *
 * Input:  10
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Use Math.abs() and the modulo operator %.
 * The main method handles input/output — don't change it.
 */
public class Warmup05LastDigit {

    /**
     * Return the last digit of n (always non-negative).
     *
     * @param n the input integer
     * @return the last digit of n
     */
    public static int solve(int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
