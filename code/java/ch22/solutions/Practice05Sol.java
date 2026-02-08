package ch22.solutions;

import java.util.*;

/**
 * Solution for Practice 5: Remove All Adjacent Duplicates in String
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Stack — push chars, pop when top matches current.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice05Sol {
    public static String solve(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == ch) {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.pollLast());
        return sb.toString();
    }
}
