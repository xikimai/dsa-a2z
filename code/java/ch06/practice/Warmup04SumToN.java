package ch06.practice;

import java.util.*;

/**
 * Warmup 04: Sum of 1 to N
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Compute the sum 1 + 2 + ... + n using THREE different methods:
 *   1. Loop method:   O(n) — iterate and accumulate
 *   2. Formula method: O(1) — use n*(n+1)/2
 *   3. Nested method:  O(n^2) — nested loop (count how many j <= i)
 *
 * Return all three results as an array. They should all be the same!
 * The point is to see that the SAME answer can come from very different
 * algorithms with very different speeds.
 *
 * INPUT FORMAT
 * ------------
 * A single integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print three space-separated integers: loop_result formula_result nested_result
 *
 * CONSTRAINTS
 * -----------
 * 0 <= n <= 10000
 *
 * EXAMPLES
 * --------
 * Input: 10     Output: 55 55 55
 * Input: 1      Output: 1 1 1
 * Input: 0      Output: 0 0 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new int[]{0, 0, 0};" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup04SumToN {

    /**
     * Compute sum 1..n three ways.
     *
     * @param n the upper bound
     * @return array of {loop_result, formula_result, nested_result}
     */
    public static int[] solve(int n) {
        // TODO: Replace this with your solution
        return new int[]{0, 0, 0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int[] result = solve(n);
        System.out.println(result[0] + " " + result[1] + " " + result[2]);
        sc.close();
    }
}
