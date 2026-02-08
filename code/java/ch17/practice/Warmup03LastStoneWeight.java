package ch17.practice;

import java.util.*;

/**
 * Warmup 3: Last Stone Weight
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Smash two heaviest stones each turn. Return last stone weight (or 0).
 * EXAMPLES:
 *   solve([2,7,4,1,8,1]) -> 1
 *   solve([1]) -> 1
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03LastStoneWeight {
    public static int solve(int[] stones) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] stones = new int[parts.length];
        for (int i = 0; i < parts.length; i++) stones[i] = Integer.parseInt(parts[i]);
        System.out.println(solve(stones));
        sc.close();
    }
}
