package ch20.solutions;

import java.util.*;

public class Warmup01Sol {
    public static int[][] solve(int[][] image, int sr, int sc, int color) {
        int rows = image.length, cols = image[0].length;
        int original = image[sr][sc];
        if (original == color) return image;

        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{sr, sc});
        image[sr][sc] = color;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int d = 0; d < 4; d++) {
                int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && image[nr][nc] == original) {
                    image[nr][nc] = color;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return image;
    }
}
