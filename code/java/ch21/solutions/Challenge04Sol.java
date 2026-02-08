package ch21.solutions;

import java.util.*;

/**
 * Solution for Challenge 4: Flatten a Multilevel Doubly Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(d) recursion depth
 */
public class Challenge04Sol {
    @SuppressWarnings("unchecked")
    public static List<Integer> solve(List<Object> nested) {
        List<Integer> result = new ArrayList<>();
        for (Object item : nested) {
            if (item instanceof List) {
                result.addAll(solve((List<Object>) item));
            } else {
                result.add((Integer) item);
            }
        }
        return result;
    }
}
