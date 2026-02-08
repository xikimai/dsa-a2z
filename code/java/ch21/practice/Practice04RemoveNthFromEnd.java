package ch21.practice;

import java.util.*;

/**
 * Practice 4: Remove Nth Node From End
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Remove the nth node from end, return result as array.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04RemoveNthFromEnd {
    public static int[] solve(int[] arr, int n) {
        // TODO: Replace this with your solution
        return new int[]{};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sz = sc.nextInt();
        int[] arr = new int[sz];
        for (int i = 0; i < sz; i++) arr[i] = sc.nextInt();
        int n = sc.nextInt();
        System.out.println(Arrays.toString(solve(arr, n)));
        sc.close();
    }
}
