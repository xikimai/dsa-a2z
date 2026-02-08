package ch14.practice;

import java.util.*;

/**
 * Practice 1: Equilibrium Index
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Find the first index where left sum == right sum. Return -1 if none.
 *
 * EXAMPLES:
 *   solve([-7,1,5,2,-4,3,0]) -> 3
 *   solve([1,2,3])           -> -1
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01EquilibriumIndex {
    public static int solve(int[] arr) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
