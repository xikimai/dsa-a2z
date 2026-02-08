package ch12.practice;

import java.util.*;

/**
 * Practice 1: Single Number
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Every element appears twice except one. Find it.
 * EXAMPLES:
 *   solve([4,1,2,1,2]) -> 4
 *   solve([2,2,1])      -> 1
 * CONSTRAINTS: 1 <= nums.length <= 3*10^4
 */
public class Practice01SingleNumber {
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println(solve(nums));
        sc.close();
    }
}
