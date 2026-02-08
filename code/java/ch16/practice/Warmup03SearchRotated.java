package ch16.practice;

import java.util.*;

/**
 * Warmup 3: Search in Rotated Sorted Array
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Given rotated sorted array (no duplicates) and target,
 *          return index of target or -1.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03SearchRotated {
    public static int solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int target = sc.nextInt();
        System.out.println(solve(arr, target));
        sc.close();
    }
}
