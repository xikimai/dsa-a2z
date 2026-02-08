package ch17.solutions;

import java.util.*;

/**
 * Solution for Warmup 3: Last Stone Weight
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Max-heap. Pop two largest, push difference if nonzero.
 * TIME:  O(n log n)
 * SPACE: O(n)
 */
public class Warmup03Sol {
    public static int solve(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) maxHeap.add(s);
        while (maxHeap.size() > 1) {
            int first = maxHeap.poll();
            int second = maxHeap.poll();
            if (first != second) maxHeap.add(first - second);
        }
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] stones = new int[parts.length];
        for (int i = 0; i < parts.length; i++) stones[i] = Integer.parseInt(parts[i]);
        System.out.println(solve(stones));
        sc.close();
    }
}
