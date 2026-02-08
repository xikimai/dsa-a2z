package ch21.practice;

import java.util.*;

/**
 * Challenge 2: Intersection of Two Lists
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Find the intersection value of two lists, or -1.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02Intersection {
    public static int solve(int[] arrA, int[] arrB, int skipA, int skipB) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int na = sc.nextInt();
        int[] arrA = new int[na];
        for (int i = 0; i < na; i++) arrA[i] = sc.nextInt();
        int nb = sc.nextInt();
        int[] arrB = new int[nb];
        for (int i = 0; i < nb; i++) arrB[i] = sc.nextInt();
        int skipA = sc.nextInt(), skipB = sc.nextInt();
        System.out.println(solve(arrA, arrB, skipA, skipB));
        sc.close();
    }
}
