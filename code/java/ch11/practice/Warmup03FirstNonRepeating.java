package ch11.practice;

import java.util.*;

/**
 * Warmup 3: First Non-Repeating Character
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given a string, find the first character that appears exactly once.
 *          Return it as a string. If no such character exists, return "_".
 *
 * EXAMPLES:
 *   solve("aabbcdd") -> "c"
 *   solve("aabb")    -> "_"
 *   solve("abcabc")  -> "_"
 *   solve("a")       -> "a"
 *   solve("")        -> "_"
 *
 * CONSTRAINTS:
 *   - 0 <= s.length <= 10^5
 *   - s consists of lowercase English letters
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03FirstNonRepeating {
    public static String solve(String s) {
        // TODO: Replace this with your solution
        return "_";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
