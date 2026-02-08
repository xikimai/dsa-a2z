package ch21.practice;

import java.util.*;

/**
 * Practice 5: Palindrome Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Check if linked list built from array is a palindrome.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05Palindrome {
    public static boolean solve(int[] arr) {
        // TODO: Replace this with your solution
        return false;
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
