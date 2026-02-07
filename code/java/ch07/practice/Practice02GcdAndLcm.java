package ch07.practice;

import java.util.*;

/**
 * Practice 02: GCD and LCM
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given two non-negative integers a and b, return an array
 *          containing [gcd(a,b), lcm(a,b)].
 *          Use the Euclidean algorithm for GCD.
 *          LCM = a / gcd * b  (divide first to avoid overflow).
 *          If gcd is 0, lcm is 0.
 *
 * EXAMPLES:
 *   solve(12, 18)  = [6, 36]
 *   solve(7, 13)   = [1, 91]
 *   solve(0, 5)    = [5, 0]
 *   solve(100, 75) = [25, 300]
 *
 * CONSTRAINTS:
 *   0 <= a, b <= 10^18
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 * Use long to avoid overflow!
 */
public class Practice02GcdAndLcm {
    public static long[] solve(long a, long b) {
        // TODO: Replace this with your solution
        return new long[]{0, 0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = Long.parseLong(sc.nextLine().trim());
        long b = Long.parseLong(sc.nextLine().trim());
        long[] result = solve(a, b);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
