package ch07.practice;

import java.util.*;

/**
 * Practice 03: Modular Exponentiation
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Compute (base^exp) % mod using binary exponentiation.
 *          This runs in O(log exp) time instead of O(exp).
 *
 * EXAMPLES:
 *   solve(2, 10, 1000000007)  = 1024
 *   solve(2, 20, 1000000007)  = 1048576
 *   solve(123456789, 0, 1000000007) = 1
 *   solve(2, 100, 1000000007) = 976371285
 *
 * CONSTRAINTS:
 *   0 <= base, exp <= 10^18
 *   1 <= mod <= 10^9
 *
 * HINT: If exp is odd, multiply result by base. Then halve exp and
 *       square base. Repeat until exp is 0.
 *
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 * Use long everywhere to avoid overflow!
 */
public class Practice03ModExponentiation {
    public static long solve(long base, long exp, long mod) {
        // TODO: Replace this with your solution
        return 0;
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
