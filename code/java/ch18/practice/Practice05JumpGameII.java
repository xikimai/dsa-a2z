package ch18.practice;

import java.util.*;

/**
 * Practice 5: Jump Game II
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Minimum jumps to reach last index. Always reachable.
 *
 * EXAMPLES:
 *   solve([2,3,1,1,4]) -> 2
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05JumpGameII {
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nums));
        sc.close();
    }
}
