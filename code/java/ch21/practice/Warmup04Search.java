package ch21.practice;

import java.util.*;

/**
 * Warmup 4: Search in Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build LL from array, return true if target exists.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04Search {
    public static boolean solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int target = sc.nextInt();
        System.out.println(solve(arr, target));
        sc.close();
    }
}
