package ch17.solutions;

import java.util.*;

/**
 * Solution for Warmup 1: Kth Largest Element
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Min-heap of size k. Push all elements; pop when size > k.
 * TIME:  O(n log k)
 * SPACE: O(k)
 */
public class Warmup01Sol {
    public static int solve(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.add(num);
            if (minHeap.size() > k) minHeap.poll();
        }
        return minHeap.peek();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(nums, k));
        sc.close();
    }
}
