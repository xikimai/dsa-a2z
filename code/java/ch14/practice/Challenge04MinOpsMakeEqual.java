package ch14.practice;

import java.util.*;

/**
 * Challenge 4: Minimum Operations to Make All Elements Equal
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given a sorted array, find min operations (increment/decrement by 1)
 *          to make all elements equal to some existing element.
 *
 * EXAMPLES:
 *   solve([1,2,3]) -> 2
 *   solve([5])     -> 0
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04MinOpsMakeEqual {
    public static long solve(int[] arr) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
