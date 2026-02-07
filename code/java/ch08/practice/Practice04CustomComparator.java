package ch08.practice;

import java.util.*;

/**
 * Practice 04: Custom Comparator
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array of words, sort them by length (shortest first).
 *          If two words have the same length, sort them alphabetically.
 *
 * EXAMPLES:
 *   solve(["banana","apple","kiwi","cherry","fig"]) = ["fig","kiwi","apple","banana","cherry"]
 *   solve(["cat","bat","ant"])                       = ["ant","bat","cat"]
 *   solve(["a","bb","ccc","dd"])                     = ["a","bb","dd","ccc"]
 *   solve(["hello"])                                 = ["hello"]
 *   solve([])                                        = []
 *
 * CONSTRAINTS:
 *   0 <= words.length <= 10^4
 *
 * HINT: Use Arrays.sort with a custom Comparator.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04CustomComparator {
    public static String[] solve(String[] words) {
        // TODO: Replace this with your solution
        return new String[0];
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println();
        } else {
            String[] words = line.split("\\s+");
            String[] result = solve(words);
            StringJoiner sj = new StringJoiner(" ");
            for (String w : result) sj.add(w);
            System.out.println(sj);
        }
        sc.close();
    }
}
