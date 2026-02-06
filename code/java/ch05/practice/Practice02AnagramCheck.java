package ch05.practice;

import java.util.*;

/**
 * Practice 02: Anagram Check
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given two strings, determine if they are anagrams of each other.
 * The check should be case-insensitive.
 * Two strings are anagrams if they contain the same characters
 * with the same frequencies.
 *
 * INPUT FORMAT
 * ------------
 * Two lines, each containing a string.
 *
 * OUTPUT FORMAT
 * -------------
 * Print "true" or "false".
 *
 * CONSTRAINTS
 * -----------
 * 0 <= s1.length(), s2.length() <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:
 * listen
 * silent
 * Output: true
 *
 * Input:
 * hello
 * world
 * Output: false
 *
 * Input:
 * (empty)
 * (empty)
 * Output: true
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return false;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice02AnagramCheck {

    /**
     * Check if two strings are anagrams (case-insensitive).
     *
     * @param s1 first string
     * @param s2 second string
     * @return true if anagrams
     */
    public static boolean solve(String s1, String s2) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        System.out.println(solve(s1, s2));
        sc.close();
    }
}
