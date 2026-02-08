package ch18.practice;

import java.util.*;

/**
 * Warmup 4: Lemonade Change
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Each lemonade costs $5. Can you make change for everyone?
 *
 * EXAMPLES:
 *   solve([5,5,5,10,20])   -> true
 *   solve([5,5,10,10,20])  -> false
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04LemonadeChange {
    public static boolean solve(int[] bills) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] bills = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(bills));
        sc.close();
    }
}
