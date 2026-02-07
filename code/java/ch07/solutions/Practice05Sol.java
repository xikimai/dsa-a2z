package ch07.solutions;

import java.util.*;

/**
 * Solution for Practice 05: Trailing Zeros in n!
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Count factors of 5 in n!. Each multiple of 5 contributes at least one 5,
 * each multiple of 25 contributes an extra, each multiple of 125 another, etc.
 * Formula: n/5 + n/25 + n/125 + ...
 *
 * TIME COMPLEXITY:  O(log_5(n))
 * SPACE COMPLEXITY: O(1)
 */
public class Practice05Sol {

    public static int solve(int n) {
        int count = 0;
        long p = 5;
        while (p <= n) {
            count += (int)(n / p);
            p *= 5;
        }
        return count;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
