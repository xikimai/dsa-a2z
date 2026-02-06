package ch03.practice;

import java.util.Scanner;

/**
 * Practice 03: Reverse Number
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return the number with its digits reversed.
 * Handle negative numbers (reverse the digits, keep the sign).
 * Leading zeros after reversal are dropped (e.g., 1200 -> 21).
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the reversed number.
 *
 * CONSTRAINTS
 * -----------
 * -1,000,000 <= n <= 1,000,000
 *
 * EXAMPLES
 * --------
 * Input:  1234
 * Output: 4321
 *
 * Input:  1200
 * Output: 21
 *
 * Input:  5
 * Output: 5
 *
 * Input:  -123
 * Output: -321
 *
 * Input:  0
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * Hint: Extract the last digit with % 10, build the reversed number
 * by multiplying by 10 and adding each digit.
 * The main method handles input/output -- don't change it.
 */
public class Practice03ReverseNumber {

    /**
     * Reverse the digits of n. Preserve sign, drop leading zeros.
     *
     * @param n any integer
     * @return the reversed number
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
