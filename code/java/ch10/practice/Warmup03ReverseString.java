package ch10.practice;

import java.util.*;

/**
 * Warmup 03: Reverse String
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a string s, return it reversed using recursion.
 *
 * ALGORITHM: reverse(s) = reverse(s[1:]) + s[0], base case: length <= 1.
 *
 * EXAMPLES:
 *   solve("hello") = "olleh"
 *   solve("")      = ""
 *   solve("a")     = "a"
 *
 * CONSTRAINTS: 0 <= s.length() <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03ReverseString {
    public static String solve(String s) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
