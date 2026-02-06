package ch03.solutions;

import java.util.*;

/**
 * Solution for Warmup 04: Count Down
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a for loop starting at n and decrementing down to 1,
 * adding each value to a list.
 *
 * TIME COMPLEXITY:  O(n) — one loop from n to 1
 * SPACE COMPLEXITY: O(n) — the result list
 */
public class Warmup04Sol {

    public static List<Integer> solve(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = n; i >= 1; i--) {
            result.add(i);
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> result = solve(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(result.get(i));
        }
        System.out.println(sb.toString());
        scanner.close();
    }
}
