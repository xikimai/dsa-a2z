package ch22.solutions;

import java.util.*;

/**
 * Solution for Practice 2: Evaluate Reverse Polish Notation
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Stack — push numbers, pop two on operator, push result.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice02Sol {
    public static int solve(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+": { int b = stack.pop(), a = stack.pop(); stack.push(a + b); break; }
                case "-": { int b = stack.pop(), a = stack.pop(); stack.push(a - b); break; }
                case "*": { int b = stack.pop(), a = stack.pop(); stack.push(a * b); break; }
                case "/": { int b = stack.pop(), a = stack.pop(); stack.push(a / b); break; }
                default: stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }
}
