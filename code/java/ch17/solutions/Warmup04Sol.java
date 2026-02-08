package ch17.solutions;

import java.util.*;

/**
 * Solution for Warmup 4: Check if Array is a Min-Heap
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Check each parent against its children.
 * TIME:  O(n)
 * SPACE: O(1)
 */
public class Warmup04Sol {
    public static boolean solve(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n / 2; i++) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            if (left < n && arr[i] > arr[left]) return false;
            if (right < n && arr[i] > arr[right]) return false;
        }
        return true;
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
