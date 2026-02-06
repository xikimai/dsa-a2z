package ch04.practice;

import java.util.Scanner;

/**
 * Warmup 04: Repeat String
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that repeats a string n times (concatenated together).
 * Then write an overloaded version that defaults to repeating 3 times.
 *
 * This demonstrates Java's method overloading as an alternative to
 * Python's default parameters.
 *
 * INPUT FORMAT
 * ------------
 * Two lines:
 *   Line 1: the string to repeat
 *   Line 2: the number of times to repeat (integer)
 *
 * OUTPUT FORMAT
 * -------------
 * Print the repeated string.
 *
 * CONSTRAINTS
 * -----------
 * - n >= 0
 * - s is a non-empty string
 *
 * EXAMPLES
 * --------
 * Input:  ha
 *         3
 * Output: hahaha
 *
 * Input:  ab
 *         5
 * Output: ababababab
 *
 * Input:  xyz
 *         0
 * Output: (empty line)
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement solve(String s, int n) — the main version.
 * 2. Implement solve(String s) — calls the first with n=3.
 * The main method handles input/output -- don't change it.
 */
public class Warmup04RepeatString {

    /**
     * Repeat string s exactly n times.
     *
     * @param s the string to repeat
     * @param n how many times to repeat
     * @return the repeated string
     */
    public static String solve(String s, int n) {
        // TODO: Replace this with your solution
        return "";
    }

    /**
     * Repeat string s exactly 3 times (overloaded default).
     *
     * @param s the string to repeat
     * @return the string repeated 3 times
     */
    public static String solve(String s) {
        // TODO: Replace this — hint: call the other solve()
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(s, n));
        sc.close();
    }
}
