package ch28.solutions;

import java.util.*;

public class Practice01Sol {
    // Alien Dictionary
    public static String solve(String[] words) {
        Set<Character> chars = new HashSet<>();
        for (String w : words)
            for (char c : w.toCharArray()) chars.add(c);

        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> inDeg = new HashMap<>();
        for (char c : chars) { adj.put(c, new HashSet<>()); inDeg.put(c, 0); }

        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            if (w1.length() > w2.length() && w1.startsWith(w2)) return "";
            int len = Math.min(w1.length(), w2.length());
            for (int j = 0; j < len; j++) {
                char c1 = w1.charAt(j), c2 = w2.charAt(j);
                if (c1 != c2) {
                    if (!adj.get(c1).contains(c2)) {
                        adj.get(c1).add(c2);
                        inDeg.put(c2, inDeg.get(c2) + 1);
                    }
                    break;
                }
            }
        }

        Queue<Character> queue = new ArrayDeque<>();
        for (char c : chars)
            if (inDeg.get(c) == 0) queue.add(c);

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            char c = queue.poll();
            sb.append(c);
            for (char nxt : adj.get(c)) {
                inDeg.put(nxt, inDeg.get(nxt) - 1);
                if (inDeg.get(nxt) == 0) queue.add(nxt);
            }
        }
        return sb.length() == chars.size() ? sb.toString() : "";
    }
}
