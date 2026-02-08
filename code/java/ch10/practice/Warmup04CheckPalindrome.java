package ch10.practice;

import java.util.*;

/**
 * Warmup 04: Check Palindrome
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a string s, return true if it is a palindrome, false otherwise.
 *          Use recursion to compare characters from both ends.
 *
 * ALGORITHM: Compare first and last characters. If they match, recurse on
 *            the substring without those two characters.
 *
 * EXAMPLES:
 *   solve("racecar") = true
 *   solve("hello")   = false
 *   solve("")        = true
 *   solve("a")       = true
 *
 * CONSTRAINTS: 0 <= s.length() <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04CheckPalindrome {
    public static boolean solve(String s) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
