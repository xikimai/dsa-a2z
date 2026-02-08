package ch18.practice;

import java.util.*;

/**
 * Practice 4: Non-overlapping Intervals
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min intervals to remove so rest don't overlap.
 *
 * EXAMPLES:
 *   solve([[1,2],[2,3],[3,4],[1,3]]) -> 1
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04NonOverlappingIntervals {
    public static int solve(int[][] intervals) {
        // TODO: Replace this with your solution
        return 0;
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
        System.out.println(solve(intervals));
        sc.close();
    }
}
