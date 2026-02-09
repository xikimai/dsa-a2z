package ch27.solutions;

import java.util.*;

public class Practice05Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        int INF = (int) 1e9;
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, INF);
        dist[0][0] = grid[0][0];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{grid[0][0], 0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int d = top[0], r = top[1], c = top[2];
            if (d > dist[r][c]) continue;
            if (r == n - 1 && c == n - 1) return d;
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int nd = Math.max(d, grid[nr][nc]);
                    if (nd < dist[nr][nc]) {
                        dist[nr][nc] = nd;
                        pq.offer(new int[]{nd, nr, nc});
                    }
                }
            }
        }
        return dist[n - 1][n - 1];
    }
}
