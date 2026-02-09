package ch32.solutions;

public class Warmup02Sol {
    static int[][] children = new int[200001][26];
    static int[] count = new int[200001];
    static int nodeCount = 0;

    static int newNode() {
        int id = ++nodeCount;
        for (int i = 0; i < 26; i++) children[id][i] = 0;
        count[id] = 0;
        return id;
    }

    public static int[] solve(String[] words, String[] prefixes) {
        nodeCount = 0;
        int root = newNode();
        for (String word : words) {
            int node = root;
            for (char ch : word.toCharArray()) {
                int idx = ch - 'a';
                if (children[node][idx] == 0)
                    children[node][idx] = newNode();
                node = children[node][idx];
                count[node]++;
            }
        }
        int[] result = new int[prefixes.length];
        for (int q = 0; q < prefixes.length; q++) {
            int node = root;
            boolean found = true;
            for (char ch : prefixes[q].toCharArray()) {
                int idx = ch - 'a';
                if (children[node][idx] == 0) { found = false; break; }
                node = children[node][idx];
            }
            result[q] = found ? count[node] : 0;
        }
        return result;
    }
}
