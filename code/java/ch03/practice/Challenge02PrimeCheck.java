package ch03.practice;

import java.util.Scanner;

/**
 * Challenge 02: Prime Check
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return true if n is a prime number, false otherwise.
 * A prime number is greater than 1 and has no divisors other than 1 and
 * itself.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print "true" or "false".
 *
 * CONSTRAINTS
 * -----------
 * -1,000,000 <= n <= 1,000,000
 *
 * EXAMPLES
 * --------
 * Input:  2
 * Output: true
 *
 * Input:  17
 * Output: true
 *
 * Input:  4
 * Output: false
 *
 * Input:  1
 * Output: false
 *
 * Input:  -5
 * Output: false
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return false;" in the solve() method with your solution.
 * Hint: Only check divisors up to sqrt(n). If any divisor from 2 to
 * sqrt(n) divides n evenly, it's not prime.
 * The main method handles input/output -- don't change it.
 */
public class Challenge02PrimeCheck {

    /**
     * Check if n is a prime number.
     *
     * @param n any integer
     * @return true if n is prime, false otherwise
     */
    public static boolean solve(int n) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
