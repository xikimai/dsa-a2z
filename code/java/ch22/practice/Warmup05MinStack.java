package ch22.practice;

import java.util.*;

/**
 * Warmup 5: Min Stack
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement a stack supporting push, pop, top, getMin in O(1).
 *          Operations given as String[][]. Return results for top/getMin.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05MinStack {
    public static List<Integer> solve(String[][] operations) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        String[][] ops = {{"push","-2"},{"push","0"},{"push","-3"},
                          {"getMin","0"},{"pop","0"},{"top","0"},{"getMin","0"}};
        System.out.println(solve(ops));
    }
}
