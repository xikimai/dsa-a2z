package ch18.practice;

import java.util.*;

/**
 * Warmup 2: Jump Game I
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Can you reach the last index? nums[i] = max jump from i.
 *
 * EXAMPLES:
 *   solve([2,3,1,1,4]) -> true
 *   solve([3,2,1,0,4]) -> false
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02JumpGame {
    public static boolean solve(int[] nums) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nums));
        sc.close();
    }
}
