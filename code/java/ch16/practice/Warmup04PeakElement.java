package ch16.practice;

import java.util.*;

/**
 * Warmup 4: Peak Element in Array
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find index of any peak element (greater than its neighbors).
 *          Treat out-of-bounds as negative infinity.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04PeakElement {
    public static int solve(int[] arr) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
