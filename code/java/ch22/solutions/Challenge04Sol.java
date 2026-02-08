package ch22.solutions;

import java.util.*;

/**
 * Solution for Challenge 4: LRU Cache
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * APPROACH: LinkedHashMap with access-order.
 * TIME:  O(1) per operation
 * SPACE: O(capacity)
 */
public class Challenge04Sol {
    public static List<Integer> solve(int capacity, String[][] operations) {
        LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity;
            }
        };
        List<Integer> results = new ArrayList<>();

        for (String[] op : operations) {
            if (op[0].equals("get")) {
                int key = Integer.parseInt(op[1]);
                results.add(cache.getOrDefault(key, -1));
            } else if (op[0].equals("put")) {
                int key = Integer.parseInt(op[1]);
                int value = Integer.parseInt(op[2]);
                cache.put(key, value);
            }
        }
        return results;
    }
}
