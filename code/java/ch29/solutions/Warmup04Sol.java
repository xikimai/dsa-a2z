package ch29.solutions;

import java.util.*;

public class Warmup04Sol {
    // Prim's MST
    @SuppressWarnings("unchecked")
    public static int solve(int n, int[][] edges) {
        if (n <= 1) return 0;
        List<int[]>[] adj = new List[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[2], e[1]});
            adj[e[1]].add(new int[]{e[2], e[0]});
        }
        boolean[] vis = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});
        int total = 0, count = 0;
        while (!pq.isEmpty() && count < n) {
            int[] top = pq.poll();
            if (vis[top[1]]) continue;
            vis[top[1]] = true;
            total += top[0];
            count++;
            for (int[] nb : adj[top[1]])
                if (!vis[nb[1]]) pq.offer(nb);
        }
        return total;
    }
}
