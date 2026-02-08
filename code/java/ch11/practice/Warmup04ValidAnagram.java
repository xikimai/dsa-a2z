package ch11.practice;

import java.util.*;

/**
 * Warmup 4: Valid Anagram
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given two strings s1 and s2, determine if s2 is an anagram of s1.
 *          Two strings are anagrams if they contain the same characters
 *          with the same frequencies. Comparison is case-sensitive.
 *
 * EXAMPLES:
 *   solve("listen", "silent") -> true
 *   solve("hello", "world")   -> false
 *   solve("", "")             -> true
 *   solve("ab", "ba")         -> true
 *   solve("abc", "abd")       -> false
 *
 * CONSTRAINTS:
 *   - 0 <= s1.length, s2.length <= 10^5
 *   - s1 and s2 consist of lowercase English letters
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04ValidAnagram {
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
