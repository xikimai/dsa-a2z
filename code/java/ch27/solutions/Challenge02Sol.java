package ch27.solutions;

import java.util.*;

public class Challenge02Sol {
    public static int[] solve(int n, int[][] redEdges, int[][] blueEdges) {
        // adj[node][color] = list of neighbors. 0=red, 1=blue
        List<Integer>[][] adj = new ArrayList[n][2];
        for (int i = 0; i < n; i++) {
            adj[i][0] = new ArrayList<>();
            adj[i][1] = new ArrayList<>();
        }
        for (int[] e : redEdges) adj[e[0]][0].add(e[1]);
        for (int[] e : blueEdges) adj[e[0]][1].add(e[1]);

        int INF = (int) 1e9;
        int[][] dist = new int[n][2];
        for (int[] row : dist) Arrays.fill(row, INF);
        dist[0][0] = 0;
        dist[0][1] = 0;

        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0}); // node, last color
        q.offer(new int[]{0, 1});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int u = cur[0], color = cur[1];
            int nextColor = 1 - color;
            for (int v : adj[u][nextColor]) {
                if (dist[u][color] + 1 < dist[v][nextColor]) {
                    dist[v][nextColor] = dist[u][color] + 1;
                    q.offer(new int[]{v, nextColor});
                }
            }
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int best = Math.min(dist[i][0], dist[i][1]);
            result[i] = best >= INF ? -1 : best;
        }
        return result;
    }
}
