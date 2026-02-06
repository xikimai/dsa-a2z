package ch05.practice;

import java.util.*;

/**
 * Warmup 03: Count Vowels
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given a string, count the number of vowels (a, e, i, o, u).
 * The check should be case-insensitive.
 *
 * INPUT FORMAT
 * ------------
 * A single line of text.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the count of vowels.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= s.length() <= 10^5
 * s contains printable ASCII characters.
 *
 * EXAMPLES
 * --------
 * Input:  Hello World
 * Output: 3
 *
 * Input:  aeiou
 * Output: 5
 *
 * Input:  xyz
 * Output: 0
 *
 * Input:  (empty)
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup03CountVowels {

    /**
     * Count the number of vowels in the string (case-insensitive).
     *
     * @param s the input string
     * @return number of vowels
     */
    public static int solve(String s) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        System.out.println(solve(line));
        sc.close();
    }
}
