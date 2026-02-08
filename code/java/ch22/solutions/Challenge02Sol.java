package ch22.solutions;

import java.util.*;

/**
 * Solution for Challenge 2: Trapping Rain Water
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Two-pointer technique with left_max and right_max.
 * TIME:  O(n)
 * SPACE: O(1)
 */
public class Challenge02Sol {
    public static int solve(int[] height) {
        if (height.length < 3) return 0;
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int water = 0;

        while (left < right) {
            if (leftMax <= rightMax) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
            }
        }
        return water;
    }
}
