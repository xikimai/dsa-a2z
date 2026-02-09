package ch29.solutions;

import java.util.*;

public class Practice02Sol {
    // Accounts Merge
    static int[] parent, rank;

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
    }

    public static List<List<String>> solve(List<List<String>> accounts) {
        Map<String, Integer> emailToId = new HashMap<>();
        Map<String, String> emailToName = new HashMap<>();
        int id = 0;

        // Assign IDs to emails
        for (List<String> acc : accounts) {
            String name = acc.get(0);
            for (int i = 1; i < acc.size(); i++) {
                String email = acc.get(i);
                if (!emailToId.containsKey(email)) {
                    emailToId.put(email, id++);
                }
                emailToName.put(email, name);
            }
        }

        parent = new int[id];
        rank = new int[id];
        for (int i = 0; i < id; i++) parent[i] = i;

        // Union emails within same account
        for (List<String> acc : accounts) {
            int firstId = emailToId.get(acc.get(1));
            for (int i = 2; i < acc.size(); i++)
                union(firstId, emailToId.get(acc.get(i)));
        }

        // Group emails by root
        Map<Integer, TreeSet<String>> groups = new HashMap<>();
        for (String email : emailToId.keySet()) {
            int root = find(emailToId.get(email));
            groups.computeIfAbsent(root, k -> new TreeSet<>()).add(email);
        }

        // Build result
        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, TreeSet<String>> entry : groups.entrySet()) {
            List<String> merged = new ArrayList<>();
            String firstEmail = entry.getValue().first();
            merged.add(emailToName.get(firstEmail));
            merged.addAll(entry.getValue());
            result.add(merged);
        }
        result.sort((a, b) -> a.get(1).compareTo(b.get(1)));
        return result;
    }
}
