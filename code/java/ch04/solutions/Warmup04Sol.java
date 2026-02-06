package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 04: Repeat String
 * =======================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a StringBuilder to concatenate the string n times.
 * The overloaded solve(String s) calls solve(s, 3) to default to 3 repeats.
 * This shows Java's method overloading as an alternative to Python's
 * default parameters.
 *
 * TIME COMPLEXITY:  O(n * len(s))
 * SPACE COMPLEXITY: O(n * len(s)) for the result string
 */
public class Warmup04Sol {

    public static String solve(String s, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(s);
        }
        return sb.toString();
    }

    public static String solve(String s) {
        return solve(s, 3);
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
