package ch02.practice;

import java.util.Scanner;

/**
 * Warmup 04: Swap Two Numbers
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given two integers a and b, swap them and return {b, a}.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing two space-separated integers: a and b.
 *
 * OUTPUT FORMAT
 * -------------
 * Print two space-separated integers — b then a (the swapped values).
 *
 * CONSTRAINTS
 * -----------
 * -10^6 <= a, b <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  3 7
 * Output: 7 3
 *
 * Input:  -1 5
 * Output: 5 -1
 *
 * Input:  0 0
 * Output: 0 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return an int array with two elements: {b, a}.
 * The main method handles input/output — don't change it.
 */
public class Warmup04Swap {

    /**
     * Swap two numbers and return them in reversed order.
     *
     * @param a the first integer
     * @param b the second integer
     * @return an int array {b, a}
     */
    public static int[] solve(int a, int b) {
        // TODO: Replace this with your solution
        return new int[]{0, 0};
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
