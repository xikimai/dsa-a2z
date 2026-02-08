package ch21.practice;

import java.util.*;

/**
 * Warmup 5: Reverse a Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build LL from array, reverse it, return result as array.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05Reverse {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
