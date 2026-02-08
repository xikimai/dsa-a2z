package ch16.practice;

import java.util.*;

/**
 * Practice 1: Koko Eating Bananas
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Koko eats bananas at speed k per hour (one pile at a time).
 *          Return minimum k to finish all piles within h hours.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01KokoBananas {
    public static int solve(int[] piles, int h) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] piles = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int h = sc.nextInt();
        System.out.println(solve(piles, h));
        sc.close();
    }
}
