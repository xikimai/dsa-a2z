package ch19.solutions;

import java.util.*;

public class Challenge02Sol {
    public static boolean solve(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
        }
        int[] state = new int[numCourses]; // 0=unvisited, 1=in_progress, 2=done
        for (int c = 0; c < numCourses; c++) {
            if (state[c] == 0) {
                if (hasCycle(adj, c, state)) return false;
            }
        }
        return true;
    }

    private static boolean hasCycle(List<List<Integer>> adj, int node, int[] state) {
        state[node] = 1;
        for (int nb : adj.get(node)) {
            if (state[nb] == 1) return true;
            if (state[nb] == 0 && hasCycle(adj, nb, state)) return true;
        }
        state[node] = 2;
        return false;
    }
}
