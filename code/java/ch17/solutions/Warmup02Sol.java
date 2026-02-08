package ch17.solutions;

import java.util.*;

/**
 * Solution for Warmup 2: Sort Using Heap (Heapsort)
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Add all to PriorityQueue, poll all out.
 * TIME:  O(n log n)
 * SPACE: O(n)
 */
public class Warmup02Sol {
    public static int[] solve(int[] arr) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int x : arr) pq.add(x);
        int[] result = new int[arr.length];
        for (int i = 0; i < result.length; i++) result[i] = pq.poll();
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(Arrays.toString(solve(new int[0])));
        } else {
            String[] parts = line.split(" ");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            System.out.println(Arrays.toString(solve(arr)));
        }
        sc.close();
    }
}
