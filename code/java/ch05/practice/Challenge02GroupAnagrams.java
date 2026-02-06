package ch05.practice;

import java.util.*;

/**
 * Challenge 02: Group Anagrams
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of strings, group the anagrams together.
 * Each group should be sorted alphabetically internally, and the
 * groups should be sorted by their first element.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated strings (lowercase letters only).
 *
 * OUTPUT FORMAT
 * -------------
 * Print each group on its own line, space-separated.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= strs.length <= 10^4
 * 0 <= strs[i].length() <= 100
 * strs[i] consists of lowercase English letters.
 *
 * EXAMPLES
 * --------
 * Input:  eat tea tan ate nat bat
 * Output:
 * ate eat tea
 * bat
 * nat tan
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new ArrayList<>();" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Challenge02GroupAnagrams {

    /**
     * Group anagrams together. Inner lists sorted, outer sorted by first element.
     *
     * @param strs array of strings
     * @return list of groups (each group is a sorted list of anagrams)
     */
    public static List<List<String>> solve(String[] strs) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().trim().split("\\s+");
        List<List<String>> result = solve(strs);
        for (List<String> group : result) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < group.size(); i++) {
                if (i > 0) sb.append(" ");
                sb.append(group.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
