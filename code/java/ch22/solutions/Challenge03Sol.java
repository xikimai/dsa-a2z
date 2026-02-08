package ch22.solutions;

import java.util.*;

/**
 * Solution for Challenge 3: Online Stock Span
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Monotonic stack storing [price, span] pairs.
 * TIME:  O(1) amortized per call
 * SPACE: O(n)
 */
public class Challenge03Sol {
    public static int[] solve(int[] prices) {
        Deque<int[]> stack = new ArrayDeque<>(); // {price, span}
        int[] result = new int[prices.length];

        for (int i = 0; i < prices.length; i++) {
            int span = 1;
            while (!stack.isEmpty() && stack.peek()[0] <= prices[i]) {
                span += stack.pop()[1];
            }
            stack.push(new int[]{prices[i], span});
            result[i] = span;
        }
        return result;
    }
}
