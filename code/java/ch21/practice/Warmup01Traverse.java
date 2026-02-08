package ch21.practice;

import java.util.*;

/**
 * Warmup 1: Traverse Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build a linked list from an array, traverse it, return values as array.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01Traverse {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] result = solve(arr);
        System.out.println(Arrays.toString(result));
        sc.close();
    }
}
