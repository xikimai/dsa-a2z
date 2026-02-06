package ch03.solutions;

import java.util.*;

/**
 * Solution for Warmup 06: Multiplication Table
 * ==============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Loop from 1 to 10, building a formatted string for each row.
 * The format is "i x n = result".
 *
 * TIME COMPLEXITY:  O(1) — always exactly 10 iterations
 * SPACE COMPLEXITY: O(1) — the list always has exactly 10 elements
 */
public class Warmup06Sol {

    public static List<String> solve(int n) {
        List<String> table = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            table.add(i + " x " + n + " = " + (i * n));
        }
        return table;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<String> table = solve(n);
        for (String line : table) {
            System.out.println(line);
        }
        scanner.close();
    }
}
