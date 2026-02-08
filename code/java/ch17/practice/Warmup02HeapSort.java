package ch17.practice;

import java.util.*;

/**
 * Warmup 2: Sort Using Heap (Heapsort)
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Sort an array in ascending order using a heap.
 * EXAMPLES:
 *   solve([5,3,8,1,2]) -> [1,2,3,5,8]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02HeapSort {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
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
