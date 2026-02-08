package ch10.solutions;

import java.util.*;

/**
 * Solution for Warmup 05: Power (Exponentiation)
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Simple recursion. Base case: base^0 = 1.
 *           Recursive case: base^exp = base * base^(exp-1).
 *
 * TIME COMPLEXITY:  O(exp)
 * SPACE COMPLEXITY: O(exp) — call stack depth
 */
public class Warmup05Sol {

    public static long solve(int base, int exp) {
        if (exp == 0) return 1;
        return (long) base * solve(base, exp - 1);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int base = Integer.parseInt(sc.nextLine().trim());
        int exp = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(base, exp));
        sc.close();
    }
}
