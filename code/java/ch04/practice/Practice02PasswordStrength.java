package ch04.practice;

import java.util.Scanner;

/**
 * Practice 02: Password Strength
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that evaluates password strength as "weak", "medium",
 * or "strong" based on these rules:
 *
 *   - "weak":   length < 8
 *   - "medium": length >= 8, has digit OR has uppercase (but not both)
 *   - "strong": length >= 8, has BOTH a digit AND an uppercase letter
 *
 * Use helper functions hasDigit() and hasUpper() to check conditions.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing the password (no spaces).
 *
 * OUTPUT FORMAT
 * -------------
 * Print "weak", "medium", or "strong".
 *
 * EXAMPLES
 * --------
 * Input:  abc
 * Output: weak
 *
 * Input:  abcdefgh
 * Output: weak
 *
 * Input:  abcdefg1
 * Output: medium
 *
 * Input:  Abcdefgh
 * Output: medium
 *
 * Input:  Abcdefg1
 * Output: strong
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement hasDigit() — returns true if any char is a digit.
 * 2. Implement hasUpper() — returns true if any char is uppercase.
 * 3. Implement solve() using those helpers.
 * The main method handles input/output -- don't change it.
 */
public class Practice02PasswordStrength {

    /**
     * Check if the string contains at least one digit (0-9).
     *
     * @param s the string to check
     * @return true if s contains a digit
     */
    public static boolean hasDigit(String s) {
        // TODO: Implement
        return false;
    }

    /**
     * Check if the string contains at least one uppercase letter (A-Z).
     *
     * @param s the string to check
     * @return true if s contains an uppercase letter
     */
    public static boolean hasUpper(String s) {
        // TODO: Implement
        return false;
    }

    /**
     * Evaluate password strength.
     *
     * @param password the password to evaluate
     * @return "weak", "medium", or "strong"
     */
    public static String solve(String password) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String password = sc.nextLine().trim();
        System.out.println(solve(password));
        sc.close();
    }
}
