package ch07.practice;

import java.util.*;

/**
 * Practice 01: All Divisors
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given a positive integer n, return a sorted list of ALL
 *          its divisors.
 *
 * EXAMPLES:
 *   solve(36) = [1, 2, 3, 4, 6, 9, 12, 18, 36]
 *   solve(1)  = [1]
 *   solve(7)  = [1, 7]
 *   solve(12) = [1, 2, 3, 4, 6, 12]
 *
 * CONSTRAINTS:
 *   1 <= n <= 10^9
 *
 * HINT: You only need to check up to sqrt(n). If i divides n,
 *       then n/i also divides n.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01AllDivisors {
    public static List<Integer> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
