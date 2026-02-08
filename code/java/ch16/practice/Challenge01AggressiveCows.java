package ch16.practice;

import java.util.*;

/**
 * Challenge 1: Aggressive Cows
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Place c cows in stalls to maximize the minimum distance
 *          between any two cows.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01AggressiveCows {
    public static int solve(int[] stalls, int cows) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] stalls = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int cows = sc.nextInt();
        System.out.println(solve(stalls, cows));
        sc.close();
    }
}
