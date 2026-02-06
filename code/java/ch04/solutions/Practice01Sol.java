package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 01: Calculator
 * =====================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Define separate helper methods for add, subtract, multiply, and divide.
 * Use a switch/if-else to dispatch to the right helper based on the
 * operator string. Return null for invalid operators or divide-by-zero.
 *
 * TIME COMPLEXITY:  O(1) — single arithmetic operation
 * SPACE COMPLEXITY: O(1)
 */
public class Practice01Sol {

    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static Integer divide(int a, int b) {
        if (b == 0) return null;
        return a / b;
    }

    public static Integer solve(int a, String op, int b) {
        switch (op) {
            case "+": return add(a, b);
            case "-": return subtract(a, b);
            case "*": return multiply(a, b);
            case "/": return divide(a, b);
            default:  return null;
        }
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
