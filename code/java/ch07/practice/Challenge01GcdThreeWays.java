package ch07.practice;

import java.util.*;

/**
 * Challenge 01: GCD Three Ways
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Implement GCD using three different algorithms:
 *
 * 1. solveSubtract(a, b): Repeated subtraction.
 *    While a != b, subtract the smaller from the larger.
 *
 * 2. solveEuclidean(a, b): Euclidean algorithm.
 *    Replace a with b, and b with a % b, until b is 0.
 *
 * 3. solveExtended(a, b): Extended Euclidean algorithm.
 *    Return [gcd, x, y] such that a*x + b*y = gcd(a,b).
 *
 * 4. solve(a, b): Default — just call solveEuclidean.
 *
 * EXAMPLES:
 *   solveSubtract(48, 18) = 6
 *   solveEuclidean(7, 13) = 1
 *   solveExtended(35, 15) = [5, 1, -2]  (35*1 + 15*(-2) = 5)
 *
 * CONSTRAINTS:
 *   0 <= a, b <= 10^18  (subtraction only tested with small inputs)
 *
 * INSTRUCTIONS: Replace the bodies of all four methods with your solutions.
 */
public class Challenge01GcdThreeWays {

    public static long solveSubtract(long a, long b) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static long solveEuclidean(long a, long b) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static long[] solveExtended(long a, long b) {
        // TODO: Replace this with your solution
        // Return [gcd, x, y] such that a*x + b*y = gcd
        return new long[]{0, 0, 0};
    }

    public static long solve(long a, long b) {
        return solveEuclidean(a, b);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = Long.parseLong(sc.nextLine().trim());
        long b = Long.parseLong(sc.nextLine().trim());
        long[] ext = solveExtended(a, b);
        System.out.println("Subtract:  " + solveSubtract(a, b));
        System.out.println("Euclidean: " + solveEuclidean(a, b));
        System.out.printf("Extended:  gcd=%d, x=%d, y=%d%n", ext[0], ext[1], ext[2]);
        sc.close();
    }
}
