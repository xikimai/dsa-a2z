package ch12.practice;

import java.util.*;

/**
 * Challenge 1: Single Number — Three Ways (AOPS Showcase)
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Find single element using three approaches:
 *   solveSort, solveHash, solveXor
 * CONSTRAINTS: 1 <= nums.length <= 3*10^4
 */
public class Challenge01SingleNumberThreeWays {
    public static int solveSort(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static int solveHash(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static int solveXor(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println("Sort: " + solveSort(nums.clone()));
        System.out.println("Hash: " + solveHash(nums.clone()));
        System.out.println("XOR:  " + solveXor(nums.clone()));
        sc.close();
    }
}
