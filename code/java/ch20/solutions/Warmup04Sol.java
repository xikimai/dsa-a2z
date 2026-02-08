package ch20.solutions;

import java.util.*;

public class Warmup04Sol {
    public static char[][] solve(char[][] board) {
        int rows = board.length, cols = board[0].length;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ((r == 0 || r == rows - 1 || c == 0 || c == cols - 1) && board[r][c] == 'O') {
                    queue.add(new int[]{r, c});
                    board[r][c] = 'S';
                }

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int d = 0; d < 4; d++) {
                int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'O') {
                    board[nr][nc] = 'S';
                    queue.add(new int[]{nr, nc});
                }
            }
        }

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == 'S') board[r][c] = 'O';
            }
        return board;
    }
}
