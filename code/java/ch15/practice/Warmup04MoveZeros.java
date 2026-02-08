package ch15.practice;

import java.util.*;

/**
 * Warmup 4: Move Zeros to End
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Move all zeros to the end while maintaining order of non-zero elements.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04MoveZeros {
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
