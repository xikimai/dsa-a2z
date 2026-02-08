package ch18.practice;

import java.util.*;

/**
 * Challenge 1: Job Sequencing with Deadlines
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Maximize profit scheduling jobs with deadlines (1 unit each).
 *
 * EXAMPLES:
 *   solve([[1,4,20],[2,1,10],[3,1,40],[4,1,30]]) -> [2, 60]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01JobSequencing {
    public static int[] solve(int[][] jobs) {
        // TODO: Replace this with your solution
        return new int[]{0, 0};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            jobs[i][0] = Integer.parseInt(parts[0]);
            jobs[i][1] = Integer.parseInt(parts[1]);
            jobs[i][2] = Integer.parseInt(parts[2]);
        }
        int[] result = solve(jobs);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
