package ch03.practice;

import java.util.Scanner;

/**
 * Warmup 01: Even or Odd
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return "Even" if n is even, or "Odd" if n is odd.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print "Even" or "Odd".
 *
 * CONSTRAINTS
 * -----------
 * n can be any integer (positive, negative, or zero).
 *
 * EXAMPLES
 * --------
 * Input:  4
 * Output: Even
 *
 * Input:  7
 * Output: Odd
 *
 * Input:  0
 * Output: Even
 *
 * Input:  -3
 * Output: Odd
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * Hint: Use the modulo operator (%).
 * The main method handles input/output -- don't change it.
 */
public class Warmup01EvenOdd {

    /**
     * Determine if n is even or odd.
     *
     * @param n any integer
     * @return "Even" or "Odd"
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
