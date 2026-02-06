package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 05: Sum 1 to N
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a loop to accumulate the sum from 1 to n.
 *
 * Bonus: There's a famous formula n*(n+1)/2 discovered by young Gauss.
 * The loop version is O(n), while the formula is O(1). Both are fine
 * here — the loop teaches you the pattern, the formula teaches you
 * to look for shortcuts.
 *
 * TIME COMPLEXITY:  O(n) — loop version; O(1) with formula
 * SPACE COMPLEXITY: O(1) — just an accumulator variable
 */
public class Warmup05Sol {

    public static int solve(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
