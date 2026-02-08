package ch22.solutions;

import java.util.*;

/**
 * Solution for Warmup 4: Next Greater Element
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Monotonic stack, process right to left.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Warmup04Sol {
    public static int[] solve(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] <= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) result[i] = arr[stack.peek()];
            stack.push(i);
        }
        return result;
    }
}
