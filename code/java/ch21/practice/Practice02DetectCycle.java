package ch21.practice;

import java.util.*;

/**
 * Practice 2: Detect Cycle
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Build LL with cycle at cyclePos, return true if cycle exists.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02DetectCycle {
    public static boolean solve(int[] arr, int cyclePos) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int cyclePos = sc.nextInt();
        System.out.println(solve(arr, cyclePos));
        sc.close();
    }
}
