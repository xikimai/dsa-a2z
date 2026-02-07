package ch07.practice;

import java.util.*;

/**
 * Challenge 03: GCD Pair Sum
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given an array of positive integers, compute the sum of
 *          gcd(nums[i], nums[j]) for all pairs where i < j.
 *
 * EXAMPLES:
 *   solve([2, 4, 6])     = 6    (gcd(2,4)=2 + gcd(2,6)=2 + gcd(4,6)=2)
 *   solve([3, 6, 9])     = 9    (gcd(3,6)=3 + gcd(3,9)=3 + gcd(6,9)=3)
 *   solve([12, 18, 24])  = 24   (gcd(12,18)=6 + gcd(12,24)=12 + gcd(18,24)=6)
 *   solve([7])            = 0    (no pairs)
 *   solve([2, 3, 5, 7])  = 6    (all pairwise gcds are 1, six pairs)
 *
 * CONSTRAINTS:
 *   1 <= nums.length <= 1000
 *   1 <= nums[i] <= 10^6
 *
 * HINT: Brute force works here — try all O(n^2) pairs. Use your
 *       Euclidean GCD as a helper.
 *
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 */
public class Challenge03GcdPairSum {
    public static long solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }
        System.out.println(solve(nums));
        sc.close();
    }
}
