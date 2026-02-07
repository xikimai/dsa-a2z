package ch08.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: Sort By Frequency
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * 1. Build a frequency map using HashMap.
 * 2. Box int[] to Integer[] so we can use a custom Comparator.
 * 3. Sort with comparator: primary = -frequency (descending),
 *    secondary = value (ascending).
 * 4. Unbox back to int[].
 *
 * TIME COMPLEXITY:  O(n log n)
 * SPACE COMPLEXITY: O(n)
 */
public class Challenge03Sol {

    public static int[] solve(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : arr) freq.merge(v, 1, Integer::sum);

        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];

        Arrays.sort(boxed, (a, b) -> {
            int fa = freq.get(a), fb = freq.get(b);
            if (fa != fb) return fb - fa; // higher frequency first
            return a - b;                 // same frequency: smaller value first
        });

        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) result[i] = boxed[i];
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println();
        } else {
            String[] parts = line.split("\\s+");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            int[] result = solve(arr);
            StringJoiner sj = new StringJoiner(" ");
            for (int v : result) sj.add(String.valueOf(v));
            System.out.println(sj);
        }
        sc.close();
    }
}
