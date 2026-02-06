package ch03.practice;

import java.util.*;

/**
 * Practice 01: FizzBuzz
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a list of strings from 1 to n where:
 *   - Multiples of 3 and 5 become "FizzBuzz"
 *   - Multiples of 3 (only) become "Fizz"
 *   - Multiples of 5 (only) become "Buzz"
 *   - All other numbers become their string representation
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print each value on a new line.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 10,000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output:
 *   1
 *   2
 *   Fizz
 *   4
 *   Buzz
 *
 * Input:  15
 * Output: (ends with) ... 13 14 FizzBuzz
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a list of strings representing the FizzBuzz sequence.
 * Hint: Check divisibility by 15 first, then by 3, then by 5.
 * The main method handles input/output -- don't change it.
 */
public class Practice01Fizzbuzz {

    /**
     * Return the FizzBuzz sequence from 1 to n.
     *
     * @param n the upper bound (inclusive)
     * @return list of FizzBuzz strings
     */
    public static List<String> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
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
