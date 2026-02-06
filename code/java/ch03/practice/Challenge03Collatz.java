package ch03.practice;

import java.util.*;

/**
 * Challenge 03: Collatz Sequence
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return the Collatz sequence starting at n
 * and ending at 1. The Collatz rule is:
 *   - If the current number is even, divide it by 2.
 *   - If the current number is odd, multiply by 3 and add 1.
 * Repeat until you reach 1.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the Collatz sequence, space-separated.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 1,000,000
 *
 * EXAMPLES
 * --------
 * Input:  6
 * Output: 6 3 10 5 16 8 4 2 1
 *
 * Input:  1
 * Output: 1
 *
 * Input:  2
 * Output: 2 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a list of integers representing the Collatz sequence.
 * Hint: Use a while loop that continues until the number equals 1.
 * The main method handles input/output -- don't change it.
 */
public class Challenge03Collatz {

    /**
     * Return the Collatz sequence starting at n.
     *
     * @param n a positive integer
     * @return list of integers in the Collatz sequence from n to 1
     */
    public static List<Integer> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
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
