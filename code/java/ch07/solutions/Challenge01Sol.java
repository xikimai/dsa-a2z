package ch07.solutions;

import java.util.*;

/**
 * Solution for Challenge 01: GCD Three Ways
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * Three GCD algorithms:
 * 1. Subtraction: O(max(a,b)) — simple but slow
 * 2. Euclidean:   O(log(min(a,b))) — the standard approach
 * 3. Extended:    O(log(min(a,b))) — also finds Bezout coefficients x, y
 */
public class Challenge01Sol {

    public static long solveSubtract(long a, long b) {
        if (a == 0) return b;
        if (b == 0) return a;
        while (a != b) {
            if (a > b) a -= b;
            else b -= a;
        }
        return a;
    }

    public static long solveEuclidean(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static long[] solveExtended(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] r = solveExtended(b, a % b);
        long x = r[2];
        long y = r[1] - (a / b) * r[2];
        return new long[]{r[0], x, y};
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
