package ch17.solutions;

import java.util.*;

/**
 * Solution for Challenge 1: Reorganize String
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Max-heap of (count, char). Greedily place most frequent,
 *           push previous back if it still has count.
 * TIME:  O(n log 26) = O(n)
 * SPACE: O(1) auxiliary
 */
public class Challenge01Sol {
    public static String solve(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;

        int maxCount = 0;
        for (int f : freq) maxCount = Math.max(maxCount, f);
        if (maxCount > (s.length() + 1) / 2) return "";

        // Max-heap: (-count, char)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> b[0] - a[0]
        );
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) pq.add(new int[]{freq[i], i});
        }

        StringBuilder result = new StringBuilder();
        int[] prev = {0, -1};

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            result.append((char)(curr[1] + 'a'));
            if (prev[0] > 0) pq.add(prev);
            prev = new int[]{curr[0] - 1, curr[1]};
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(solve(sc.nextLine().trim()));
        sc.close();
    }
}
