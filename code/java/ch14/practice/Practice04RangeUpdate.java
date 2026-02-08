package ch14.practice;

import java.util.*;

/**
 * Practice 4: Range Update with Difference Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Start with n zeros. Apply updates [l, r, val] (add val to range).
 *          Return final array.
 *
 * EXAMPLES:
 *   solve(5, [[1,3,2],[2,4,3],[0,1,-1]]) -> [-1, 1, 5, 5, 3]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04RangeUpdate {
    public static long[] solve(int n, int[][] updates) {
        // TODO: Replace this with your solution
        return new long[n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int q = Integer.parseInt(sc.nextLine().trim());
        int[][] updates = new int[q][3];
        for (int i = 0; i < q; i++) {
            String[] parts = sc.nextLine().split(" ");
            updates[i][0] = Integer.parseInt(parts[0]);
            updates[i][1] = Integer.parseInt(parts[1]);
            updates[i][2] = Integer.parseInt(parts[2]);
        }
        System.out.println(Arrays.toString(solve(n, updates)));
        sc.close();
    }
}
