package ch05.solutions;

import java.util.*;

/**
 * Solution for Practice 05: Longest Common Prefix
 * =================================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Character-by-character comparison: use the first string as a reference.
 * For each character position, check if all other strings have the same
 * character at that position. Stop as soon as a mismatch is found or
 * any string runs out of characters.
 *
 * TIME COMPLEXITY:  O(S) where S is the sum of all string lengths
 * SPACE COMPLEXITY: O(1) beyond the input (we build the prefix incrementally)
 */
public class Practice05Sol {

    public static String solve(String[] strs) {
        if (strs.length == 0) return "";

        String first = strs[0];
        for (int i = 0; i < first.length(); i++) {
            char c = first.charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return first.substring(0, i);
                }
            }
        }
        return first;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().trim().split("\\s+");
        System.out.println(solve(strs));
        sc.close();
    }
}
