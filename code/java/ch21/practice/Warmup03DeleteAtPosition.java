package ch21.practice;

import java.util.*;

/**
 * Warmup 3: Delete Node at Position
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build LL from array, delete node at pos, return result as array.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03DeleteAtPosition {
    public static int[] solve(int[] arr, int pos) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int pos = sc.nextInt();
        System.out.println(Arrays.toString(solve(arr, pos)));
        sc.close();
    }
}
