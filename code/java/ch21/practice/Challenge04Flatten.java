package ch21.practice;

import java.util.*;

/**
 * Challenge 4: Flatten a Multilevel Doubly Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * PROBLEM: Flatten a nested list (depth-first) into a single-level list.
 * Input is a nested list represented as List<Object> where each element
 * is either an Integer or a List<Object>.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04Flatten {
    @SuppressWarnings("unchecked")
    public static List<Integer> solve(List<Object> nested) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        // Simple demo
        List<Object> test = new ArrayList<>();
        test.add(1);
        test.add(2);
        List<Object> sub = new ArrayList<>();
        sub.add(3);
        sub.add(4);
        test.add(sub);
        test.add(5);
        System.out.println(solve(test));
    }
}
