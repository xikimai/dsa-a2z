package ch19.solutions;

import java.util.*;

public class Challenge01Sol {
    public static int solve(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                Queue<Integer> queue = new LinkedList<>();
                queue.add(i);
                visited[i] = true;
                while (!queue.isEmpty()) {
                    int city = queue.poll();
                    for (int j = 0; j < n; j++) {
                        if (isConnected[city][j] == 1 && !visited[j]) {
                            visited[j] = true;
                            queue.add(j);
                        }
                    }
                }
                count++;
            }
        }
        return count;
    }
}
