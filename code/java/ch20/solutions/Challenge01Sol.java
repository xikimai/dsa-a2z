package ch20.solutions;

import java.util.*;

public class Challenge01Sol {
    static final int INF = 2147483647;

    public static int[][] solve(int[][] rooms) {
        int rows = rooms.length, cols = rooms[0].length;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (rooms[r][c] == 0)
                    queue.add(new int[]{r, c});

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && rooms[nr][nc] == INF) {
                    rooms[nr][nc] = rooms[r][c] + 1;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return rooms;
    }
}
