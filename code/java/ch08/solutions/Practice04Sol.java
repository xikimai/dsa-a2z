package ch08.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Custom Comparator
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use Arrays.sort with a chained comparator:
 *   1. Primary: sort by string length (ascending)
 *   2. Secondary: sort alphabetically (natural order)
 *
 * TIME COMPLEXITY:  O(n log n)
 * SPACE COMPLEXITY: O(n) for the sorted copy
 */
public class Practice04Sol {

    public static String[] solve(String[] words) {
        String[] result = words.clone();
        Arrays.sort(result, Comparator.comparingInt(String::length)
                                      .thenComparing(Comparator.naturalOrder()));
        return result;
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
