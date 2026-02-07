package ch07.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Modular Exponentiation
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Binary exponentiation: repeatedly square the base and halve the exponent.
 * If the exponent is odd, multiply result by base. All operations mod m.
 *
 * TIME COMPLEXITY:  O(log exp)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice03Sol {

    public static long solve(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = result * base % mod;
            }
            exp /= 2;
            base = base * base % mod;
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long base = Long.parseLong(sc.nextLine().trim());
        long exp = Long.parseLong(sc.nextLine().trim());
        long mod = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(base, exp, mod));
        sc.close();
    }
}
