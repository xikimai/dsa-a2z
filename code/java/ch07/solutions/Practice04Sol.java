package ch07.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Prime Factorization
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Trial division: for each potential divisor d from 2 to sqrt(n),
 * count how many times d divides n. If n > 1 after the loop,
 * the remaining n is a prime factor.
 *
 * TIME COMPLEXITY:  O(sqrt(n))
 * SPACE COMPLEXITY: O(number of prime factors)
 */
public class Practice04Sol {

    public static List<int[]> solve(long n) {
        List<int[]> factors = new ArrayList<>();
        for (long d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                int count = 0;
                while (n % d == 0) {
                    count++;
                    n /= d;
                }
                factors.add(new int[]{(int) d, count});
            }
        }
        if (n > 1) {
            factors.add(new int[]{(int) n, 1});
        }
        return factors;
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
