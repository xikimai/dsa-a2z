package ch28.solutions;

import java.util.*;

public class Warmup01Sol {
    // Topological Sort using Kahn's Algorithm
    public static int[] solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDeg = new int[n];
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            inDeg[e[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            if (inDeg[i] == 0) queue.add(i);
        int[] result = new int[n];
        int idx = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            result[idx++] = u;
            for (int v : adj.get(u))
                if (--inDeg[v] == 0) queue.add(v);
        }
        return idx == n ? result : new int[0];
    }
}
