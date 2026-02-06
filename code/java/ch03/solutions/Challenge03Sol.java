package ch03.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: Collatz Sequence
 * =============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Start with n, add it to the list, then apply the Collatz rules
 * repeatedly until we reach 1:
 *   - If even: divide by 2
 *   - If odd: multiply by 3 and add 1
 *
 * The Collatz conjecture says this always reaches 1, but nobody has
 * proven it yet! It's one of the great unsolved problems in math.
 *
 * TIME COMPLEXITY:  O(?) — unknown! The number of steps is not predictable.
 *                   For n < 1,000,000, it's always reasonable.
 * SPACE COMPLEXITY: O(k) — where k is the number of steps to reach 1
 */
public class Challenge03Sol {

    public static List<Integer> solve(int n) {
        List<Integer> sequence = new ArrayList<>();
        sequence.add(n);
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            sequence.add(n);
        }
        return sequence;
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
