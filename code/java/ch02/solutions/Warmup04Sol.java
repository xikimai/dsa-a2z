package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 04: Swap Two Numbers
 * ==========================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Return a new array with the values in reversed order: {b, a}.
 * In Java, we can't directly swap two variables and return them,
 * so we use an array to return both values.
 *
 * TIME COMPLEXITY:  O(1) — just creating a small array
 * SPACE COMPLEXITY: O(1) — the array has exactly 2 elements
 */
public class Warmup04Sol {

    /**
     * Swap two numbers and return them in reversed order.
     *
     * @param a the first integer
     * @param b the second integer
     * @return an int array {b, a}
     */
    public static int[] solve(int a, int b) {
        return new int[]{b, a};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int[] result = solve(a, b);
        System.out.println(result[0] + " " + result[1]);
        scanner.close();
    }
}
