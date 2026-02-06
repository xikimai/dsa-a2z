package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Challenge 01: Prime Check (Three Ways)
 * =====================================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three progressively better approaches:
 *
 * V1 — Brute force: Check every number from 2 to n-1.
 *       Time: O(n)
 *
 * V2 — Square root: If n = a * b, one factor must be <= sqrt(n).
 *       Time: O(sqrt(n))
 *
 * V3 — 6k +/- 1: All primes > 3 are of the form 6k +/- 1.
 *       Check 2, 3, then only 6k-1 and 6k+1 up to sqrt(n).
 *       Time: O(sqrt(n)) with ~3x fewer iterations than V2.
 *
 * TIME COMPLEXITY:  O(sqrt(n)) using V3
 * SPACE COMPLEXITY: O(1)
 */
public class Challenge01Sol {

    public static boolean isPrimeV1(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static boolean isPrimeV2(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static boolean isPrimeV3(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    public static boolean solve(int n) {
        return isPrimeV3(n);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solve(n));
        sc.close();
    }
}
