package ch08.solutions;

import java.util.*;

/**
 * Solution for Warmup 05: Sort By Absolute Value
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Box int[] to Integer[], sort with Comparator.comparingInt(Math::abs),
 * then unbox back to int[]. Arrays.sort on objects is stable, so equal
 * absolute values preserve original order.
 *
 * TIME COMPLEXITY:  O(n log n)
 * SPACE COMPLEXITY: O(n)
 */
public class Warmup05Sol {

    public static int[] solve(int[] arr) {
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];
        Arrays.sort(boxed, Comparator.comparingInt(Math::abs));
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
