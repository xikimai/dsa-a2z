package ch03.practice;

import java.util.Scanner;

/**
 * Warmup 02: Absolute Value
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return its absolute value without using Math.abs().
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the absolute value of n.
 *
 * CONSTRAINTS
 * -----------
 * -1,000,000 <= n <= 1,000,000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output: 5
 *
 * Input:  -5
 * Output: 5
 *
 * Input:  0
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Use an if/else to check if n is negative.
 * Do NOT use Math.abs() -- that's the whole point of this exercise!
 * The main method handles input/output -- don't change it.
 */
public class Warmup02AbsoluteValue {

    /**
     * Return the absolute value of n without using Math.abs().
     *
     * @param n any integer
     * @return absolute value of n
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
