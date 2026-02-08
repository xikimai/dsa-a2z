package ch22.solutions;

import java.util.*;

/**
 * Solution for Warmup 3: Implement Queue Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Use ArrayDeque for O(1) enqueue/dequeue.
 * TIME:  O(1) per operation
 * SPACE: O(n)
 */
public class Warmup03Sol {
    public static List<Integer> solve(String[][] operations) {
        Deque<Integer> q = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : operations) {
            switch (op[0]) {
                case "enqueue":
                    q.offerLast(Integer.parseInt(op[1]));
                    break;
                case "dequeue":
                    if (q.isEmpty()) { results.add(-1); }
                    else { results.add(q.pollFirst()); }
                    break;
                case "front":
                    if (q.isEmpty()) { results.add(-1); }
                    else { results.add(q.peekFirst()); }
                    break;
                case "is_empty":
                    results.add(q.isEmpty() ? 1 : 0);
                    break;
            }
        }
        return results;
    }
}
