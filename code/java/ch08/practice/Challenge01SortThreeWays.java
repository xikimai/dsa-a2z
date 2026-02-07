package ch08.practice;

import java.util.*;

/**
 * Challenge 01: Sort Three Ways
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Implement three different sorting algorithms and compare them.
 *          All three must produce the same sorted output.
 *
 * METHODS:
 *   solveBubble(arr)  — Bubble sort
 *   solveMerge(arr)   — Merge sort
 *   solveBuiltin(arr) — Java's Arrays.sort
 *   solve(arr)        — Default, calls solveMerge
 *
 * EXAMPLES:
 *   solveBubble([5, 3, 8, 1, 2])  = [1, 2, 3, 5, 8]
 *   solveMerge([5, 3, 8, 1, 2])   = [1, 2, 3, 5, 8]
 *   solveBuiltin([5, 3, 8, 1, 2]) = [1, 2, 3, 5, 8]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^4
 *
 * INSTRUCTIONS: Replace the bodies of all four methods with your solutions.
 */
public class Challenge01SortThreeWays {

    public static int[] solveBubble(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    public static int[] solveMerge(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    public static int[] solveBuiltin(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    public static int[] solve(int[] arr) {
        return solveMerge(arr);
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
