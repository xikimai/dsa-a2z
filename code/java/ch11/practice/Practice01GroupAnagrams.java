package ch11.practice;

import java.util.*;

/**
 * Practice 1: Group Anagrams
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an array of strings, group the anagrams together.
 *          Each inner group should be sorted alphabetically.
 *          The outer list should be sorted by each group's first element.
 *
 * EXAMPLES:
 *   solve(["eat","tea","tan","ate","nat","bat"])
 *       -> [["ate","eat","tea"], ["bat"], ["nat","tan"]]
 *   solve([""])   -> [[""]]
 *   solve(["a"])  -> [["a"]]
 *   solve([])     -> []
 *
 * HINT: Sort each string's characters to create a canonical key:
 *       char[] ca = s.toCharArray(); Arrays.sort(ca); String key = new String(ca);
 *
 * CONSTRAINTS:
 *   - 0 <= strs.length <= 10^4
 *   - 0 <= strs[i].length <= 100
 *   - strs[i] consists of lowercase English letters
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01GroupAnagrams {
    public static List<List<String>> solve(String[] strs) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String[] strs = new String[n];
        for (int i = 0; i < n; i++) strs[i] = sc.nextLine().trim();
        List<List<String>> result = solve(strs);
        for (List<String> group : result) {
            System.out.println(String.join(",", group));
        }
        sc.close();
    }
}
