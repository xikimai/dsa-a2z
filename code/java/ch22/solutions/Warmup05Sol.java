package ch22.solutions;

import java.util.*;

/**
 * Solution for Warmup 5: Min Stack
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Two stacks — main and min stack (parallel tracking).
 * TIME:  O(1) per operation
 * SPACE: O(n)
 */
public class Warmup05Sol {
    public static List<Integer> solve(String[][] operations) {
        Deque<Integer> stack = new ArrayDeque<>();
        Deque<Integer> minStack = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();

        for (String[] op : operations) {
            switch (op[0]) {
                case "push": {
                    int x = Integer.parseInt(op[1]);
                    stack.push(x);
                    if (minStack.isEmpty() || x <= minStack.peek()) {
                        minStack.push(x);
                    } else {
                        minStack.push(minStack.peek());
                    }
                    break;
                }
                case "pop":
                    stack.pop();
                    minStack.pop();
                    break;
                case "top":
                    results.add(stack.peek());
                    break;
                case "getMin":
                    results.add(minStack.peek());
                    break;
            }
        }
        return results;
    }
}
