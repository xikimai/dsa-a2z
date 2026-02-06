package ch05.practice;

import java.util.*;

/**
 * Practice 05: Longest Common Prefix
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of strings, find the longest common prefix
 * shared by all strings. If there is no common prefix, return "".
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated strings.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the longest common prefix (or empty line if none).
 *
 * CONSTRAINTS
 * -----------
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length() <= 200
 * strs[i] consists of lowercase English letters only.
 *
 * EXAMPLES
 * --------
 * Input:  flower flow flight
 * Output: fl
 *
 * Input:  dog racecar car
 * Output: (empty)
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice05LongestCommonPrefix {

    /**
     * Find the longest common prefix of the given strings.
     *
     * @param strs array of strings
     * @return the longest common prefix
     */
    public static String solve(String[] strs) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().trim().split("\\s+");
        System.out.println(solve(strs));
        sc.close();
    }
}
