package ch17.solutions;

import java.util.*;

/**
 * Solution for Practice 1: Top K Frequent Elements
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Frequency map + min-heap of size k by frequency.
 * TIME:  O(n + m log k)
 * SPACE: O(n)
 */
public class Practice01Sol {
    public static List<Integer> solve(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n, 0) + 1);

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(
                (a, b) -> freq.get(a) - freq.get(b)
        );
        for (int key : freq.keySet()) {
            minHeap.add(key);
            if (minHeap.size() > k) minHeap.poll();
        }

        List<Integer> result = new ArrayList<>(minHeap);
        Collections.sort(result);
        return result;
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
