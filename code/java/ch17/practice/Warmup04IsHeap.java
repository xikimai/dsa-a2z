package ch17.practice;

import java.util.*;

/**
 * Warmup 4: Check if Array is a Min-Heap
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Return true if array satisfies min-heap property.
 * EXAMPLES:
 *   solve([1,3,2,7,6,5,4]) -> true
 *   solve([7,3,2,1,6,5,4]) -> false
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04IsHeap {
    public static boolean solve(int[] arr) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            String[] parts = line.split(" ");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            System.out.println(solve(arr));
        }
        sc.close();
    }
}
