package ch07.practice;

import java.util.*;

/**
 * Practice 04: Prime Factorization
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given a positive integer n, return its prime factorization
 *          as a list of [prime, count] pairs, sorted by prime.
 *
 * EXAMPLES:
 *   solve(12)  = [[2,2], [3,1]]          (12 = 2^2 * 3)
 *   solve(1)   = []                       (no prime factors)
 *   solve(7)   = [[7,1]]                  (7 is prime)
 *   solve(360) = [[2,3], [3,2], [5,1]]   (360 = 2^3 * 3^2 * 5)
 *
 * CONSTRAINTS:
 *   1 <= n <= 10^12
 *
 * HINT: Trial division up to sqrt(n). For each divisor d starting
 *       from 2, count how many times d divides n. If n > 1 after
 *       the loop, it's a prime factor.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04PrimeFactorization {
    public static List<int[]> solve(long n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        List<int[]> factors = solve(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < factors.size(); i++) {
            if (i > 0) sb.append(" * ");
            sb.append(factors.get(i)[0]).append("^").append(factors.get(i)[1]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
