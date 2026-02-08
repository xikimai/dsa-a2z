package ch22.solutions;

import java.util.*;

/**
 * Solution for Practice 3: Sliding Window Maximum
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Deque maintaining decreasing order of values.
 * TIME:  O(n)
 * SPACE: O(k)
 */
public class Practice03Sol {
    public static int[] solve(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int ri = 0;

        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) result[ri++] = nums[dq.peekFirst()];
        }
        return result;
    }
}
