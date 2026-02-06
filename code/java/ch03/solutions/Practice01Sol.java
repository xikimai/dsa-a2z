package ch03.solutions;

import java.util.*;

/**
 * Solution for Practice 01: FizzBuzz
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Loop from 1 to n. For each number, check divisibility:
 *   - Divisible by both 3 AND 5 (i.e., by 15) -> "FizzBuzz"
 *   - Divisible by 3 only -> "Fizz"
 *   - Divisible by 5 only -> "Buzz"
 *   - Otherwise -> the number itself as a string
 *
 * Key insight: Check the "both" case FIRST (% 15 == 0), because if you
 * check % 3 first, you'll print "Fizz" for 15 and never reach "FizzBuzz".
 *
 * TIME COMPLEXITY:  O(n) — one pass through 1..n
 * SPACE COMPLEXITY: O(n) — the result list
 */
public class Practice01Sol {

    public static List<String> solve(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i));
            }
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<String> result = solve(n);
        for (String s : result) {
            System.out.println(s);
        }
        scanner.close();
    }
}
