package ch27.solutions;

import java.util.*;

public class Practice02Sol {
    public static int solve(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int INF = (int) 1e9;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, INF);
        dist[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int effort = top[0], r = top[1], c = top[2];
            if (effort > dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return effort;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int ne = Math.max(effort, Math.abs(heights[r][c] - heights[nr][nc]));
                    if (ne < dist[nr][nc]) {
                        dist[nr][nc] = ne;
                        pq.offer(new int[]{ne, nr, nc});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}
