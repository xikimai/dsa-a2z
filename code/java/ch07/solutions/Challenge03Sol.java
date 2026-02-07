package ch07.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: GCD Pair Sum
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Brute force: iterate all O(n^2) pairs and sum their GCDs.
 * Uses Euclidean GCD as a helper.
 *
 * TIME COMPLEXITY:  O(n^2 * log(max value))
 * SPACE COMPLEXITY: O(1)
 */
public class Challenge03Sol {

    public static long solve(int[] nums) {
        long total = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                total += gcd(nums[i], nums[j]);
            }
        }
        return total;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
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
