package ch32.solutions;

import java.util.*;

public class Challenge01Sol {
    public static List<String> solve(char[][] board, String[] words) {
        // Build Trie using HashMap
        Map<Character, Object[]> root = new HashMap<>();
        // Object[0] = children map, Object[1] = word (or null)
        for (String word : words) {
            Map<Character, Object[]> node = root;
            for (char ch : word.toCharArray()) {
                node.putIfAbsent(ch, new Object[]{new HashMap<Character, Object[]>(), null});
                Object[] arr = node.get(ch);
                node = (Map<Character, Object[]>) arr[0];
            }
            // Store word at the leaf
            // We need a wrapper since the last node's children map IS the node
        }

        // Simpler approach: nested maps with special key
        HashMap<String, Object> trie = new HashMap<>();
        for (String word : words) {
            HashMap<String, Object> node = trie;
            for (char ch : word.toCharArray()) {
                String key = String.valueOf(ch);
                node.putIfAbsent(key, new HashMap<String, Object>());
                node = (HashMap<String, Object>) node.get(key);
            }
            node.put("$", word);
        }

        int rows = board.length, cols = board[0].length;
        List<String> result = new ArrayList<>();
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                dfs(board, r, c, trie, result, rows, cols, dirs);

        Collections.sort(result);
        return result;
    }

    private static void dfs(char[][] board, int r, int c,
                            HashMap<String, Object> node, List<String> result,
                            int rows, int cols, int[][] dirs) {
        char ch = board[r][c];
        String key = String.valueOf(ch);
        if (!node.containsKey(key)) return;

        HashMap<String, Object> next = (HashMap<String, Object>) node.get(key);

        if (next.containsKey("$")) {
            result.add((String) next.get("$"));
            next.remove("$");
        }

        board[r][c] = '.';
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] != '.')
                dfs(board, nr, nc, next, result, rows, cols, dirs);
        }
        board[r][c] = ch;

        if (next.isEmpty()) node.remove(key);
    }
}
