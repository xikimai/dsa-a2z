package ch22.solutions;

import java.util.*;

/**
 * Solution for Warmup 2: Implement Stack Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: Use ArrayList as backing store.
 * TIME:  O(1) per operation (amortized)
 * SPACE: O(n)
 */
public class Warmup02Sol {
    public static List<Integer> solve(String[][] operations) {
        List<Integer> data = new ArrayList<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : operations) {
            switch (op[0]) {
                case "push":
                    data.add(Integer.parseInt(op[1]));
                    break;
                case "pop":
                    if (data.isEmpty()) { results.add(-1); }
                    else { results.add(data.remove(data.size() - 1)); }
                    break;
                case "top":
                    if (data.isEmpty()) { results.add(-1); }
                    else { results.add(data.get(data.size() - 1)); }
                    break;
                case "is_empty":
                    results.add(data.isEmpty() ? 1 : 0);
                    break;
            }
        }
        return results;
    }
}
