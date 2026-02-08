package ch16.practice;

import java.util.*;

/**
 * Practice 2: Ship Packages Within D Days
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Ship packages in order within d days.
 *          Return minimum ship capacity.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02ShipPackages {
    public static int solve(int[] weights, int d) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] weights = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int d = sc.nextInt();
        System.out.println(solve(weights, d));
        sc.close();
    }
}
