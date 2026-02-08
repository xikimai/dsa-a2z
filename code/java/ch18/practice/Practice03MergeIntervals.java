package ch18.practice;

import java.util.*;

/**
 * Practice 3: Merge Intervals
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Merge overlapping intervals.
 *
 * EXAMPLES:
 *   solve([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03MergeIntervals {
    public static int[][] solve(int[][] intervals) {
        // TODO: Replace this with your solution
        return new int[0][];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            intervals[i][0] = Integer.parseInt(parts[0]);
            intervals[i][1] = Integer.parseInt(parts[1]);
        }
        int[][] result = solve(intervals);
        for (int[] r : result) System.out.println(r[0] + " " + r[1]);
        sc.close();
    }
}
