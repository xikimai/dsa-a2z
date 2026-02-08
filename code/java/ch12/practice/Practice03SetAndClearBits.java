package ch12.practice;

import java.util.*;

/**
 * Practice 3: Set and Clear Bits
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Implement solveSet(n,i) and solveClear(n,i).
 * EXAMPLES:
 *   solveSet(42, 0)   -> 43   (set bit 0)
 *   solveClear(42, 1) -> 40   (clear bit 1)
 * CONSTRAINTS: 0 <= n <= 10^9, 0 <= i <= 30
 */
public class Practice03SetAndClearBits {
    public static int solveSet(int n, int i) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static int solveClear(int n, int i) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String op = sc.next();
        int n = sc.nextInt(), i = sc.nextInt();
        if (op.equals("set")) System.out.println(solveSet(n, i));
        else System.out.println(solveClear(n, i));
        sc.close();
    }
}
