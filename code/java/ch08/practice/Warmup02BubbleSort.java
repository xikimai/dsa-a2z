package ch08.practice;

import java.util.*;

/**
 * Warmup 02: Bubble Sort
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Implement bubble sort. Given an array of integers,
 *          return a new array sorted in ascending order using the
 *          bubble sort algorithm. Use an early-exit flag to stop
 *          if no swaps occur in a pass.
 *
 * EXAMPLES:
 *   solve([64, 34, 25, 12, 22, 11, 90]) = [11, 12, 22, 25, 34, 64, 90]
 *   solve([1, 2, 3, 4])                 = [1, 2, 3, 4]
 *   solve([2, 1])                       = [1, 2]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02BubbleSort {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
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
