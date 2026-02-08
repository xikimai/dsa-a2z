package ch15.practice;

import java.util.*;

/**
 * Warmup 3: Max Sum of Fixed Window
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Given an array and window size k, find the max sum of k consecutive elements.
 *          Return 0 if array has fewer than k elements.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03MaxSumFixedWindow {
    public static int solve(int[] arr, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = sc.nextInt();
        System.out.println(solve(arr, k));
        sc.close();
    }
}
