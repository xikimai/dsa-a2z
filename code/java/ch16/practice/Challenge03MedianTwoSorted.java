package ch16.practice;

import java.util.*;

/**
 * Challenge 3: Median of Two Sorted Arrays
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find the median of two sorted arrays in O(log(min(m,n))) time.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03MedianTwoSorted {
    public static double solve(int[] nums1, int[] nums2) {
        // TODO: Replace this with your solution
        return 0.0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] nums1 = line1.isEmpty() ? new int[]{} :
            Arrays.stream(line1.split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] nums2 = line2.isEmpty() ? new int[]{} :
            Arrays.stream(line2.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nums1, nums2));
        sc.close();
    }
}
