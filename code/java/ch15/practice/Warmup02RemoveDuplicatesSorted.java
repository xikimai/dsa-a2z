package ch15.practice;

import java.util.*;

/**
 * Warmup 2: Remove Duplicates from Sorted Array
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Given a sorted array, return a new array with duplicates removed.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02RemoveDuplicatesSorted {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
