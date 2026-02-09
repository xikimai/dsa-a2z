package ch32.solutions;

import java.util.*;

public class Warmup01Sol {
    public static boolean[] solve(String[] words, String[] queries) {
        Map<String, Object> root = new HashMap<>();
        String END = "#";
        for (String word : words) {
            Map<String, Object> node = root;
            for (char ch : word.toCharArray()) {
                String key = String.valueOf(ch);
                node.putIfAbsent(key, new HashMap<String, Object>());
                node = (Map<String, Object>) node.get(key);
            }
            node.put(END, true);
        }
        boolean[] result = new boolean[queries.length];
        for (int q = 0; q < queries.length; q++) {
            Map<String, Object> node = root;
            boolean found = true;
            for (char ch : queries[q].toCharArray()) {
                String key = String.valueOf(ch);
                if (!node.containsKey(key)) { found = false; break; }
                node = (Map<String, Object>) node.get(key);
            }
            result[q] = found && node.containsKey(END);
        }
        return result;
    }
}
