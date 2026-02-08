package ch22.practice;

import java.util.*;

/**
 * Warmup 1: Valid Parentheses
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Given a string containing '(', ')', '{', '}', '[' and ']',
 *          determine if the string is valid (properly nested and matched).
 *
 * EXAMPLES:
 *   solve("()")     -> true
 *   solve("([)]")   -> false
 *   solve("{[]}")   -> true
 *   solve("")       -> true
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01ValidParentheses {
    public static boolean solve(String s) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        System.out.println(solve(s));
        sc.close();
    }
}
