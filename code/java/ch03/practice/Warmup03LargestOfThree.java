package ch03.practice;

import java.util.Scanner;

/**
 * Warmup 03: Largest of Three
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given three integers a, b, and c, return the largest one.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing three space-separated integers a, b, c.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the largest of the three.
 *
 * CONSTRAINTS
 * -----------
 * -1,000,000 <= a, b, c <= 1,000,000
 *
 * EXAMPLES
 * --------
 * Input:  1 2 3
 * Output: 3
 *
 * Input:  3 2 1
 * Output: 3
 *
 * Input:  5 5 5
 * Output: 5
 *
 * Input:  -1 -2 -3
 * Output: -1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Use if/else to compare pairs. Don't use Math.max() yet --
 * the goal is to practice conditional logic.
 * The main method handles input/output -- don't change it.
 */
public class Warmup03LargestOfThree {

    /**
     * Return the largest of three integers.
     *
     * @param a first integer
     * @param b second integer
     * @param c third integer
     * @return the largest of a, b, c
     */
    public static int solve(int a, int b, int c) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println(solve(a, b, c));
        scanner.close();
    }
}
