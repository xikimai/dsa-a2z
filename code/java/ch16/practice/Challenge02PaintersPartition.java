package ch16.practice;

import java.util.*;

/**
 * Challenge 2: Painter's Partition
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: k painters paint n contiguous boards. Minimize the maximum
 *          section any painter paints.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02PaintersPartition {
    public static int solve(int[] boards, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] boards = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = sc.nextInt();
        System.out.println(solve(boards, k));
        sc.close();
    }
}
