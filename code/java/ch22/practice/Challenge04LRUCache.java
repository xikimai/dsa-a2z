package ch22.practice;

import java.util.*;

/**
 * Challenge 4: LRU Cache
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement an LRU cache with get(key) and put(key, value).
 *          Both operations must be O(1). When capacity is exceeded,
 *          evict the least recently used key.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04LRUCache {
    public static List<Integer> solve(int capacity, String[][] operations) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        String[][] ops = {{"put","1","1"},{"put","2","2"},{"get","1","0"},
                          {"put","3","3"},{"get","2","0"},
                          {"put","4","4"},{"get","1","0"},{"get","3","0"},{"get","4","0"}};
        System.out.println(solve(2, ops));
    }
}
