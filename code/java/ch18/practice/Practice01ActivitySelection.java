package ch18.practice;

import java.util.*;

/**
 * Practice 1: Activity Selection
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Max non-overlapping activities. Activities are [start, end).
 *
 * EXAMPLES:
 *   solve([[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]) -> 4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01ActivitySelection {
    public static int solve(int[][] activities) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int[][] activities = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            activities[i][0] = Integer.parseInt(parts[0]);
            activities[i][1] = Integer.parseInt(parts[1]);
        }
        System.out.println(solve(activities));
        sc.close();
    }
}
