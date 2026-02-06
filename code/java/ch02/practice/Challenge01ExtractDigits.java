package ch02.practice;

import java.util.Scanner;

/**
 * Challenge 01: Extract Digits
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a 3-digit integer n (between 100 and 999), extract and return
 * its hundreds digit, tens digit, and ones digit.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print three space-separated integers: hundreds tens ones
 *
 * CONSTRAINTS
 * -----------
 * 100 <= n <= 999
 *
 * EXAMPLES
 * --------
 * Input:  123
 * Output: 1 2 3
 *
 * Input:  507
 * Output: 5 0 7
 *
 * Input:  999
 * Output: 9 9 9
 *
 * Input:  100
 * Output: 1 0 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return an int array with three elements: {hundreds, tens, ones}.
 * Hint: Use integer division (/) and modulo (%).
 * The main method handles input/output — don't change it.
 */
public class Challenge01ExtractDigits {

    /**
     * Extract the hundreds, tens, and ones digits of a 3-digit number.
     *
     * @param n a 3-digit integer (100-999)
     * @return an int array {hundreds, tens, ones}
     */
    public static int[] solve(int n) {
        // TODO: Replace this with your solution
        return new int[]{0, 0, 0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] result = solve(n);
        System.out.println(result[0] + " " + result[1] + " " + result[2]);
        scanner.close();
    }
}
