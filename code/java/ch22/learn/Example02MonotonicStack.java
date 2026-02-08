package ch22.learn;

import java.util.*;

/**
 * Example 02: Monotonic Stack — Next Greater Element & Histogram
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * Demonstrates:
 *   - Next Greater Element using monotonic stack
 *   - Largest Rectangle in Histogram
 *   - Sliding Window Maximum with deque
 */
public class Example02MonotonicStack {

    public static void nextGreaterDemo() {
        System.out.println("=== Next Greater Element ===");
        int[] arr = {4, 5, 2, 10, 8};
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
        System.out.println("  Input:  " + Arrays.toString(arr));
        System.out.println("  Result: " + Arrays.toString(result));
        System.out.println();
    }

    public static void histogramDemo() {
        System.out.println("=== Largest Rectangle in Histogram ===");
        int[] heights = {2, 1, 5, 6, 2, 3};
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int curr = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > curr) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                int area = h * w;
                maxArea = Math.max(maxArea, area);
                System.out.println("  Pop h=" + h + ", w=" + w + ", area=" + area);
            }
            stack.push(i);
        }
        System.out.println("  Heights: " + Arrays.toString(heights));
        System.out.println("  Max area: " + maxArea);
        System.out.println();
    }

    public static void slidingWindowDemo() {
        System.out.println("=== Sliding Window Maximum ===");
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        Deque<Integer> dq = new ArrayDeque<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) result.add(nums[dq.peekFirst()]);
        }
        System.out.println("  Input: " + Arrays.toString(nums) + ", k=" + k);
        System.out.println("  Result: " + result);
    }

    public static void main(String[] args) {
        nextGreaterDemo();
        histogramDemo();
        slidingWindowDemo();
    }
}
