package ch04.practice;

import java.util.Scanner;

/**
 * Challenge 01: Prime Check (Three Ways)
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write THREE different prime-checking functions, each progressively
 * more efficient. Then use the best one in solve().
 *
 * Version 1 (isPrimeV1): Check all divisors from 2 to n-1.
 *   Time: O(n)
 *
 * Version 2 (isPrimeV2): Check divisors from 2 to sqrt(n).
 *   Time: O(sqrt(n))
 *
 * Version 3 (isPrimeV3): Use the 6k +/- 1 optimization.
 *   Only check 2, 3, and numbers of the form 6k-1 and 6k+1 up to sqrt(n).
 *   Time: O(sqrt(n)) but ~3x fewer iterations than V2.
 *
 * INPUT FORMAT
 * ------------
 * A single integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print "true" or "false".
 *
 * CONSTRAINTS
 * -----------
 * n can be any integer (including negative, 0, 1).
 *
 * EXAMPLES
 * --------
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
 * 1. Implement all three versions.
 * 2. Use isPrimeV3 in solve() for the best performance.
 * The main method handles input/output -- don't change it.
 */
public class Challenge01PrimeCheck {

    /**
     * V1: Brute force — check all divisors from 2 to n-1.
     *
     * @param n the number to check
     * @return true if n is prime
     */
    public static boolean isPrimeV1(int n) {
        // TODO: Implement
        return false;
    }

    /**
     * V2: Check divisors from 2 to sqrt(n).
     *
     * @param n the number to check
     * @return true if n is prime
     */
    public static boolean isPrimeV2(int n) {
        // TODO: Implement
        return false;
    }

    /**
     * V3: 6k +/- 1 optimization.
     * All primes > 3 are of the form 6k +/- 1.
     *
     * @param n the number to check
     * @return true if n is prime
     */
    public static boolean isPrimeV3(int n) {
        // TODO: Implement
        return false;
    }

    /**
     * Check if n is prime (uses the best version).
     *
     * @param n the number to check
     * @return true if n is prime
     */
    public static boolean solve(int n) {
        // TODO: Replace this with your solution (call isPrimeV3)
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solve(n));
        sc.close();
    }
}
