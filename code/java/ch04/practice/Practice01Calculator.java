package ch04.practice;

import java.util.Scanner;

/**
 * Practice 01: Calculator
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Build a simple calculator using helper functions. Write separate
 * helper methods for add, subtract, multiply, and divide. Then write
 * a solve() method that picks the right operation based on the operator
 * string.
 *
 * INPUT FORMAT
 * ------------
 * Three values on one line: int operator int
 * Example: 10 + 3
 *
 * OUTPUT FORMAT
 * -------------
 * Print the result as an integer.
 * Print "Error" for invalid operator or division by zero.
 *
 * CONSTRAINTS
 * -----------
 * - a, b are integers
 * - op is one of: "+", "-", "*", "/"
 * - Division is integer division (truncated toward zero)
 *
 * EXAMPLES
 * --------
 * Input:  10 + 3
 * Output: 13
 *
 * Input:  10 / 3
 * Output: 3
 *
 * Input:  10 / 0
 * Output: Error
 *
 * Input:  10 % 3
 * Output: Error
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement add(), subtract(), multiply(), divide() helpers.
 * 2. Implement solve() using those helpers.
 * 3. Return null for invalid operator or divide-by-zero.
 * The main method handles input/output -- don't change it.
 */
public class Practice01Calculator {

    /** Add two numbers. */
    public static int add(int a, int b) {
        // TODO: Implement
        return 0;
    }

    /** Subtract b from a. */
    public static int subtract(int a, int b) {
        // TODO: Implement
        return 0;
    }

    /** Multiply two numbers. */
    public static int multiply(int a, int b) {
        // TODO: Implement
        return 0;
    }

    /** Divide a by b (integer division). Returns null if b is 0. */
    public static Integer divide(int a, int b) {
        // TODO: Implement (return null if b == 0)
        return null;
    }

    /**
     * Perform the operation and return the result.
     *
     * @param a  first operand
     * @param op the operator: "+", "-", "*", "/"
     * @param b  second operand
     * @return the result, or null for invalid op / divide-by-zero
     */
    public static Integer solve(int a, String op, int b) {
        // TODO: Replace this with your solution
        return null;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        String op = sc.next();
        int b = sc.nextInt();
        Integer result = solve(a, op, b);
        if (result == null) {
            System.out.println("Error");
        } else {
            System.out.println(result);
        }
        sc.close();
    }
}
