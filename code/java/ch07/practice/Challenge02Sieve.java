package ch07.practice;

import java.util.*;

/**
 * Challenge 02: Sieve of Eratosthenes
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given a non-negative integer n, return a sorted list of
 *          all prime numbers up to and including n.
 *
 * EXAMPLES:
 *   solve(10) = [2, 3, 5, 7]
 *   solve(1)  = []
 *   solve(2)  = [2]
 *   solve(30) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
 *
 * CONSTRAINTS:
 *   0 <= n <= 10^7
 *
 * HINT: Create a boolean array of size n+1, initially all true.
 *       Mark 0 and 1 as false. For each prime i starting from 2,
 *       mark all multiples of i starting from i*i as composite.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02Sieve {
    public static List<Integer> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
