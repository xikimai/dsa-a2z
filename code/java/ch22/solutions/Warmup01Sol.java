package ch22.solutions;

import java.util.*;

/**
 * Solution for Warmup 1: Valid Parentheses
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Stack — push openers, pop on closers and check match.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Warmup01Sol {
    public static boolean solve(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((ch == ')' && top != '(') ||
                    (ch == ']' && top != '[') ||
                    (ch == '}' && top != '{')) return false;
            }
        }
        return stack.isEmpty();
    }
}
