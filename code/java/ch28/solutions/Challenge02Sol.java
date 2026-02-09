package ch28.solutions;

import java.util.*;

public class Challenge02Sol {
    // Find Eventual Safe States: three-color DFS
    public static List<Integer> solve(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0=white, 1=gray, 2=black
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (isSafe(i, graph, color)) result.add(i);
        return result;
    }

    private static boolean isSafe(int u, int[][] graph, int[] color) {
        if (color[u] == 1) return false; // cycle
        if (color[u] == 2) return true;  // already safe
        color[u] = 1;
        for (int v : graph[u])
            if (!isSafe(v, graph, color)) return false;
        color[u] = 2;
        return true;
    }
}
