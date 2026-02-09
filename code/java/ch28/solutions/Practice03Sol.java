package ch28.solutions;

import java.util.*;

public class Practice03Sol {
    // Find All Recipes
    public static List<String> solve(String[] recipes, String[][] ingredients,
                                     String[] supplies) {
        Set<String> recipeSet = new HashSet<>(Arrays.asList(recipes));
        Map<String, List<String>> adj = new HashMap<>();
        Map<String, Integer> inDeg = new HashMap<>();

        for (int i = 0; i < recipes.length; i++) {
            inDeg.put(recipes[i], 0);
            for (String ing : ingredients[i]) {
                adj.computeIfAbsent(ing, k -> new ArrayList<>()).add(recipes[i]);
                inDeg.merge(recipes[i], 1, Integer::sum);
            }
        }

        Queue<String> queue = new ArrayDeque<>();
        Set<String> seen = new HashSet<>(Arrays.asList(supplies));
        for (String s : supplies) queue.add(s);

        List<String> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            String item = queue.poll();
            if (recipeSet.contains(item)) result.add(item);
            if (adj.containsKey(item)) {
                for (String nxt : adj.get(item)) {
                    inDeg.put(nxt, inDeg.get(nxt) - 1);
                    if (inDeg.get(nxt) == 0 && !seen.contains(nxt)) {
                        seen.add(nxt);
                        queue.add(nxt);
                    }
                }
            }
        }
        return result;
    }
}
