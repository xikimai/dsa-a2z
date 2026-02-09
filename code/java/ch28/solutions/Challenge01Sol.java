package ch28.solutions;

import java.util.*;

public class Challenge01Sol {
    // Minimum Height Trees: iterative leaf removal
    public static List<Integer> solve(int n, int[][] edges) {
        if (n == 1) return Arrays.asList(0);

        Set<Integer>[] adj = new Set[n];
        for (int i = 0; i < n; i++) adj[i] = new HashSet<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }

        Queue<Integer> leaves = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            if (adj[i].size() == 1) leaves.add(i);

        int remaining = n;
        while (remaining > 2) {
            int size = leaves.size();
            remaining -= size;
            Queue<Integer> newLeaves = new ArrayDeque<>();
            for (int i = 0; i < size; i++) {
                int leaf = leaves.poll();
                for (int neighbor : adj[leaf]) {
                    adj[neighbor].remove(leaf);
                    if (adj[neighbor].size() == 1) newLeaves.add(neighbor);
                }
            }
            leaves = newLeaves;
        }
        return new ArrayList<>(leaves);
    }
}
