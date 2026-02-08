package ch12.practice;

import java.util.*;

/**
 * Challenge 2: Two Numbers Appearing Odd Times
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Find two elements appearing odd times. Return sorted.
 * EXAMPLES:
 *   solve([2,4,7,9,2,4]) -> [7,9]
 * CONSTRAINTS: 2 <= nums.length <= 3*10^4
 */
public class Challenge02TwoOddOccurring {
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        int[] result = solve(nums);
        System.out.println(Arrays.toString(result));
        sc.close();
    }
}
