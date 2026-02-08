package ch19.solutions;

import java.util.*;

public class Warmup01Sol {
    public static List<List<Integer>> solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        for (List<Integer> neighbors : adj) Collections.sort(neighbors);
        return adj;
    }
}
