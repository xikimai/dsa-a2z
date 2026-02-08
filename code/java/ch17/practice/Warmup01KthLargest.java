package ch17.practice;

import java.util.*;

/**
 * Warmup 1: Kth Largest Element
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Given an unsorted array and integer k, return the kth largest element.
 * EXAMPLES:
 *   solve([3,2,1,5,6,4], 2) -> 5
 *   solve([3,2,3,1,2,4,5,5,6], 4) -> 4
 * CONSTRAINTS: 1 <= k <= nums.length <= 10^5
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01KthLargest {
    public static int solve(int[] nums, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(nums, k));
        sc.close();
    }
}
