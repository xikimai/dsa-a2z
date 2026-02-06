package ch03.practice;

import java.util.Scanner;

/**
 * Challenge 01: Diamond Pattern
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a diamond pattern made of '*'
 * characters. The diamond has (2*n - 1) rows:
 *   - The top half (rows 1 to n) grows from 1 star to (2*n - 1) stars.
 *   - The bottom half (rows n+1 to 2*n-1) shrinks back to 1 star.
 * Each row is centered with leading spaces, but NO trailing spaces.
 * Lines are separated by '\n'. No trailing newline.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the diamond pattern.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 25
 *
 * EXAMPLES
 * --------
 * Input:  1
 * Output: *
 *
 * Input:  2
 * Output:
 *  *
 * ***
 *  *
 *
 * Input:  3
 * Output:
 *   *
 *  ***
 * *****
 *  ***
 *   *
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * Hint: The top half is like a centered triangle growing. The bottom
 * half is the same triangle shrinking. Use (n-row) spaces for leading
 * padding and (2*row - 1) stars for each row number.
 * The main method handles input/output -- don't change it.
 */
public class Challenge01Diamond {

    /**
     * Return a diamond pattern with n rows in the top half.
     *
     * @param n half-height of the diamond
     * @return multi-line diamond string (no trailing spaces or newline)
     */
    public static String solve(int n) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
