package ch05.solutions;

import java.util.*;

/**
 * Solution for Challenge 02: Group Anagrams
 * ==========================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * For each string, sort its characters to create a canonical key.
 * Group strings by this key using a TreeMap (so groups are ordered).
 * Sort each group internally, then return all groups.
 *
 * TIME COMPLEXITY:  O(n * k log k) where n is number of strings, k is max length
 * SPACE COMPLEXITY: O(n * k)
 */
public class Challenge02Sol {

    public static List<List<String>> solve(String[] strs) {
        TreeMap<String, List<String>> groups = new TreeMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        List<List<String>> result = new ArrayList<>();
        for (List<String> group : groups.values()) {
            Collections.sort(group);
            result.add(group);
        }

        // Sort outer list by first element of each group
        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().trim().split("\\s+");
        List<List<String>> result = solve(strs);
        for (List<String> group : result) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < group.size(); i++) {
                if (i > 0) sb.append(" ");
                sb.append(group.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
