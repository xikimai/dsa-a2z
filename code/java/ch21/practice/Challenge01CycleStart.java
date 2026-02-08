package ch21.practice;

import java.util.*;

/**
 * Challenge 1: Find Cycle Start
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Return the index where the cycle starts, or -1.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01CycleStart {
    public static int solve(int[] arr, int cyclePos) {
        // TODO: Replace this with your solution
        return -1;
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
