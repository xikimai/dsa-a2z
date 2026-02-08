package ch22.solutions;

import java.util.*;

/**
 * Solution for Practice 1: Daily Temperatures
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Monotonic stack of indices, process left to right.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice01Sol {
    public static int[] solve(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int j = stack.pop();
                result[j] = i - j;
            }
            stack.push(i);
        }
        return result;
    }
}
