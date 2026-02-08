package ch17.practice;

import java.util.*;

/**
 * Challenge 3: Sliding Window Maximum
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Return maximum in each sliding window of size k.
 * EXAMPLES:
 *   solve([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03SlidingWindowMax {
    public static int[] solve(int[] nums, int k) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(Arrays.toString(solve(nums, k)));
        sc.close();
    }
}
