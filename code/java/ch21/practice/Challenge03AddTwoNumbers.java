package ch21.practice;

import java.util.*;

/**
 * Challenge 3: Add Two Numbers
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Add two numbers in reverse-digit form, return sum as array.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03AddTwoNumbers {
    public static int[] solve(int[] arr1, int[] arr2) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int[] arr1 = new int[n1];
        for (int i = 0; i < n1; i++) arr1[i] = sc.nextInt();
        int n2 = sc.nextInt();
        int[] arr2 = new int[n2];
        for (int i = 0; i < n2; i++) arr2[i] = sc.nextInt();
        System.out.println(Arrays.toString(solve(arr1, arr2)));
        sc.close();
    }
}
