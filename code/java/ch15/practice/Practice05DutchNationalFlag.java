package ch15.practice;

import java.util.*;

/**
 * Practice 5: Dutch National Flag
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Sort an array of 0s, 1s, and 2s in one pass.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05DutchNationalFlag {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
