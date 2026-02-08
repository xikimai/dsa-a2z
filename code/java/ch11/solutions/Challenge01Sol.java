package ch11.solutions;

import java.util.*;

/**
 * Solution for Challenge 1: Missing Number — Four Ways (AOPS Showcase)
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * Four approaches to the same problem, demonstrating different CS techniques.
 *
 * APPROACH 1 (Sort):  O(n log n) time, O(1) extra space
 * APPROACH 2 (XOR):   O(n) time, O(1) space
 * APPROACH 3 (Math):  O(n) time, O(1) space
 * APPROACH 4 (Hash):  O(n) time, O(n) space
 */
public class Challenge01Sol {
    public static int solveSort(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 0; i < sorted.length; i++) {
            if (sorted[i] != i) return i;
        }
        return sorted.length;
    }

    public static int solveXor(int[] nums) {
        int xor = 0;
        for (int i = 0; i <= nums.length; i++) {
            xor ^= i;
        }
        for (int x : nums) {
            xor ^= x;
        }
        return xor;
    }

    public static int solveMath(int[] nums) {
        int n = nums.length;
        long expected = (long) n * (n + 1) / 2;
        long actual = 0;
        for (int x : nums) actual += x;
        return (int) (expected - actual);
    }

    public static int solveHash(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        for (int i = 0; i <= nums.length; i++) {
            if (!set.contains(i)) return i;
        }
        return -1; // unreachable
    }

    public static int solve(int[] nums) {
        return solveMath(nums);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println(solve(nums));
        sc.close();
    }
}
