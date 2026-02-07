package ch08.practice;

import java.util.*;

/**
 * Practice 03: Dutch National Flag
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array containing only 0s, 1s, and 2s, sort it
 *          in-place in O(n) time and O(1) space using a single pass.
 *          This is the Dutch National Flag problem (Dijkstra).
 *
 * ALGORITHM: Use three pointers — lo, mid, hi.
 *            - Elements before lo are 0
 *            - Elements between lo and mid are 1
 *            - Elements after hi are 2
 *            - Elements between mid and hi are unexamined
 *
 * EXAMPLES:
 *   solve([2, 0, 2, 1, 1, 0])    = [0, 0, 1, 1, 2, 2]
 *   solve([0])                    = [0]
 *   solve([2, 1, 0])             = [0, 1, 2]
 *   solve([1, 0, 2, 1, 0, 2, 1]) = [0, 0, 1, 1, 1, 2, 2]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^5
 *   arr[i] is 0, 1, or 2
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 *               O(n) time, O(1) space, single pass.
 */
public class Practice03DutchNationalFlag {
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
