package ch22.learn;

import java.util.*;

/**
 * Example 01: Stack & Queue Basics — See LIFO and FIFO in Action
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * Demonstrates:
 *   - Stack (LIFO) using ArrayDeque
 *   - Queue (FIFO) using ArrayDeque
 *   - Balanced parentheses with a stack
 */
public class Example01StackQueueBasics {

    public static void stackDemo() {
        System.out.println("=== Stack (LIFO) Demo ===");
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(10); System.out.println("push(10) -> " + stack);
        stack.push(20); System.out.println("push(20) -> " + stack);
        stack.push(30); System.out.println("push(30) -> " + stack);
        System.out.println("peek()   -> " + stack.peek());
        System.out.println("pop()    -> " + stack.pop());
        System.out.println("After pop: " + stack);
        System.out.println();
    }

    public static void queueDemo() {
        System.out.println("=== Queue (FIFO) Demo ===");
        Queue<String> queue = new ArrayDeque<>();
        queue.offer("Alice");   System.out.println("enqueue Alice -> " + queue);
        queue.offer("Bob");     System.out.println("enqueue Bob   -> " + queue);
        queue.offer("Charlie"); System.out.println("enqueue Charlie -> " + queue);
        System.out.println("peek()   -> " + queue.peek());
        System.out.println("poll()   -> " + queue.poll());
        System.out.println("After dequeue: " + queue);
        System.out.println();
    }

    public static void balancedParens() {
        System.out.println("=== Balanced Parentheses ===");
        String[] tests = {"({[]})", "([)]", "((()))", "(((", ""};
        for (String s : tests) {
            boolean valid = isValid(s);
            System.out.println("  \"" + s + "\" -> " + (valid ? "VALID" : "INVALID"));
        }
    }

    static boolean isValid(String s) {
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

    public static void main(String[] args) {
        stackDemo();
        queueDemo();
        balancedParens();
    }
}
