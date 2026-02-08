package ch18.practice;

import java.util.*;

/**
 * Challenge 2: Gas Station
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Find starting station for circular trip. -1 if impossible.
 *
 * EXAMPLES:
 *   solve([1,2,3,4,5], [3,4,5,1,2]) -> 3
 *   solve([2,3,4], [3,4,3])         -> -1
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02GasStation {
    public static int solve(int[] gas, int[] cost) {
        // TODO: Replace this with your solution
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] gas = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] cost = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(gas, cost));
        sc.close();
    }
}
