package ch17.solutions;

import java.util.*;

/**
 * Solution for Practice 4: Find Median from Data Stream
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Two heaps — max-heap for lower, min-heap for upper.
 * TIME:  O(n log n) total
 * SPACE: O(n)
 */
public class Practice04Sol {
    public static List<Double> solve(int[] nums) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        List<Double> medians = new ArrayList<>();

        for (int num : nums) {
            maxHeap.add(num);
            if (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
                minHeap.add(maxHeap.poll());
            }
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.add(maxHeap.poll());
            } else if (minHeap.size() > maxHeap.size()) {
                maxHeap.add(minHeap.poll());
            }

            if (maxHeap.size() > minHeap.size()) {
                medians.add((double) maxHeap.peek());
            } else {
                medians.add((maxHeap.peek() + minHeap.peek()) / 2.0);
            }
        }
        return medians;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        System.out.println(solve(nums));
        sc.close();
    }
}
