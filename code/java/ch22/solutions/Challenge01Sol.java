package ch22.solutions;

import java.util.*;

/**
 * Solution for Challenge 1: Largest Rectangle in Histogram
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Monotonic stack (increasing). Sentinel flushes at end.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Challenge01Sol {
    public static int solve(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int curr = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > curr) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }
}
