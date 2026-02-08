package ch17.solutions;

import java.util.*;

/**
 * Solution for Challenge 3: Sliding Window Maximum
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Monotone decreasing deque of indices.
 * TIME:  O(n)
 * SPACE: O(k)
 */
public class Challenge03Sol {
    public static int[] solve(int[] nums, int k) {
        if (nums.length == 0) return new int[0];
        Deque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int ri = 0;

        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            }
            dq.addLast(i);
            if (dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }
            if (i >= k - 1) {
                result[ri++] = nums[dq.peekFirst()];
            }
        }
        return result;
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
