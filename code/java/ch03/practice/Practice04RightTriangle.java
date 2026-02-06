package ch03.practice;

import java.util.Scanner;

/**
 * Practice 04: Right-Aligned Triangle
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a right-aligned triangle pattern
 * of '*' characters with n rows. Each row i (1-indexed) has (n - i)
 * leading spaces followed by i stars. Lines are separated by '\n'.
 * No trailing newline.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the right-aligned triangle pattern.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 50
 *
 * EXAMPLES
 * --------
 * Input:  1
 * Output: *
 *
 * Input:  3
 * Output:
 *   *
 *  **
 * ***
 *
 * Input:  4
 * Output:
 *    *
 *   **
 *  ***
 * ****
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * Return the pattern as a single string with lines separated by '\n'.
 * Hint: Use nested loops — outer for rows, inner for spaces then stars.
 * The main method handles input/output -- don't change it.
 */
public class Practice04RightTriangle {

    /**
     * Return a right-aligned triangle pattern with n rows.
     *
     * @param n number of rows
     * @return multi-line string with the pattern (no trailing newline)
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
