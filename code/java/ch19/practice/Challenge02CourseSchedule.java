package ch19.practice;

import java.util.*;

/**
 * Challenge 2: Course Schedule
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return true if all courses can be finished (no cyclic dependency).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02CourseSchedule {
    public static boolean solve(int numCourses, int[][] prerequisites) {
        // TODO: Replace this with your solution
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numCourses = sc.nextInt(), m = sc.nextInt();
        int[][] prereqs = new int[m][2];
        for (int i = 0; i < m; i++) { prereqs[i][0] = sc.nextInt(); prereqs[i][1] = sc.nextInt(); }
        System.out.println(solve(numCourses, prereqs));
        sc.close();
    }
}
