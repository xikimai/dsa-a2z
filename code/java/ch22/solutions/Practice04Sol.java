package ch22.solutions;

import java.util.*;

/**
 * Solution for Practice 4: Queue Using Two Stacks
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: In-stack and out-stack. Transfer in->out when out is empty.
 * TIME:  O(1) amortized per operation
 * SPACE: O(n)
 */
public class Practice04Sol {
    public static List<Integer> solve(String[][] operations) {
        Deque<Integer> stackIn = new ArrayDeque<>();
        Deque<Integer> stackOut = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();

        for (String[] op : operations) {
            switch (op[0]) {
                case "enqueue":
                    stackIn.push(Integer.parseInt(op[1]));
                    break;
                case "dequeue":
                    if (stackOut.isEmpty()) {
                        while (!stackIn.isEmpty()) stackOut.push(stackIn.pop());
                    }
                    results.add(stackOut.pop());
                    break;
                case "peek":
                    if (stackOut.isEmpty()) {
                        while (!stackIn.isEmpty()) stackOut.push(stackIn.pop());
                    }
                    results.add(stackOut.peek());
                    break;
                case "empty":
                    results.add(stackIn.isEmpty() && stackOut.isEmpty() ? 1 : 0);
                    break;
            }
        }
        return results;
    }
}
