package ch21.practice;

import java.util.*;

/**
 * Practice 1: Find Middle Node
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build LL, return middle value (second middle for even length).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01FindMiddle {
    public static int solve(int[] arr) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(solve(arr));
        sc.close();
    }
}
