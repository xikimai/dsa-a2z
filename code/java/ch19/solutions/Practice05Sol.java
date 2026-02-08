package ch19.solutions;

import java.util.*;

public class Practice05Sol {
    public static List<List<Integer>> solve(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]); // directed
        }
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(adj, 0, n - 1, path, result);
        result.sort((a, b) -> {
            for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return a.size() - b.size();
        });
        return result;
    }

    private static void dfs(List<List<Integer>> adj, int node, int target,
                             List<Integer> path, List<List<Integer>> result) {
        if (node == target) {
            result.add(new ArrayList<>(path));
            return;
        }
        List<Integer> nbrs = new ArrayList<>(adj.get(node));
        Collections.sort(nbrs);
        for (int nb : nbrs) {
            path.add(nb);
            dfs(adj, nb, target, path, result);
            path.remove(path.size() - 1);
        }
    }
}
