package ch12.practice;

import java.util.*;

/**
 * Warmup 4: Check if i-th Bit Is Set
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Given n and i, determine if the i-th bit of n is set.
 * EXAMPLES:
 *   solve(42, 1) -> true   (101010, bit 1 is 1)
 *   solve(42, 2) -> false  (101010, bit 2 is 0)
 * CONSTRAINTS: 0 <= n <= 10^9, 0 <= i <= 30
 */
public class Warmup04CheckIthBit {
    public static boolean solve(int n, int i) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), i = sc.nextInt();
        System.out.println(solve(n, i));
        sc.close();
    }
}
