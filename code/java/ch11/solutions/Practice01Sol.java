package ch11.solutions;

import java.util.*;

/**
 * Solution for Practice 1: Group Anagrams
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Sort each string's characters to create a canonical key.
 *           Group strings by their key using a HashMap.
 *           Sort each group alphabetically, then sort groups by first element.
 * TIME:  O(n * k log k) where k = max string length
 * SPACE: O(n * k)
 */
public class Practice01Sol {
    public static List<List<String>> solve(String[] strs) {
        if (strs.length == 0) return new ArrayList<>();

        HashMap<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = new String(ca);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        List<List<String>> result = new ArrayList<>();
        for (List<String> group : groups.values()) {
            Collections.sort(group);
            result.add(group);
        }

        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String[] strs = new String[n];
        for (int i = 0; i < n; i++) strs[i] = sc.nextLine().trim();
        List<List<String>> result = solve(strs);
        for (List<String> group : result) {
            System.out.println(String.join(",", group));
        }
        sc.close();
    }
}
