package ch11.practice;

import java.util.*;

/**
 * Practice 5: Sort Characters by Frequency
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given a string, sort it by character frequency in descending order.
 *          Characters with the same frequency should be sorted alphabetically
 *          (ascending).
 *
 * EXAMPLES:
 *   solve("tree")   -> "eert"
 *   solve("cccaaa") -> "aaaccc"
 *   solve("aab")    -> "aab"
 *   solve("hello")  -> "lleho"
 *   solve("x")      -> "x"
 *   solve("")       -> ""
 *
 * CONSTRAINTS:
 *   - 0 <= s.length <= 5 * 10^5
 *   - s consists of lowercase and uppercase English letters and digits
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05SortCharsByFreq {
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
