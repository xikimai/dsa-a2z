package ch19.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;

        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);
        int length = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int q = 0; q < size; q++) {
                String word = queue.poll();
                if (word.equals(endWord)) return length;
                char[] chars = word.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[i] = c;
                        String next = new String(chars);
                        if (wordSet.contains(next) && !visited.contains(next)) {
                            visited.add(next);
                            queue.add(next);
                        }
                    }
                    chars[i] = original;
                }
            }
            length++;
        }
        return 0;
    }
}
