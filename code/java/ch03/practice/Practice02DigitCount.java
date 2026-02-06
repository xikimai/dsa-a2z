package ch03.practice;

import java.util.Scanner;

/**
 * Practice 02: Digit Count
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return the number of digits in n.
 * If n is 0, the digit count is 1. Handle negative numbers
 * by counting the digits of the absolute value.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the number of digits.
 *
 * CONSTRAINTS
 * -----------
 * -10,000,000 <= n <= 10,000,000
 *
 * EXAMPLES
 * --------
 * Input:  12345
 * Output: 5
 *
 * Input:  0
 * Output: 1
 *
 * Input:  9
 * Output: 1
 *
 * Input:  -42
 * Output: 2
 *
 * Input:  1000000
 * Output: 7
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Repeatedly divide by 10 and count iterations.
 * The main method handles input/output -- don't change it.
 */
public class Practice02DigitCount {

    /**
     * Return the number of digits in n.
     *
     * @param n any integer
     * @return digit count (always >= 1)
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
