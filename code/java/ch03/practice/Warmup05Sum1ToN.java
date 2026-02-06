package ch03.practice;

import java.util.Scanner;

/**
 * Warmup 05: Sum 1 to N
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a non-negative integer n, return the sum 1 + 2 + ... + n.
 * If n is 0, the sum is 0.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one non-negative integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the sum from 1 to n.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= n <= 100,000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output: 15
 *
 * Input:  1
 * Output: 1
 *
 * Input:  10
 * Output: 55
 *
 * Input:  100
 * Output: 5050
 *
 * Input:  0
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Use a loop to accumulate the sum. (There's also a formula,
 * but practice writing the loop first!)
 * The main method handles input/output -- don't change it.
 */
public class Warmup05Sum1ToN {

    /**
     * Return the sum of integers from 1 to n.
     *
     * @param n a non-negative integer
     * @return 1 + 2 + ... + n
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
