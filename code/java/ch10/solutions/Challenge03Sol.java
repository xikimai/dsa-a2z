package ch10.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: Combination Sum
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort candidates. Backtracking with a start index.
 *           At each step, try including the current candidate (reuse allowed)
 *           or move to the next candidate. This avoids duplicate combinations.
 *
 * TIME COMPLEXITY:  O(2^t) where t = target / min(candidates)
 * SPACE COMPLEXITY: O(t) — recursion depth
 */
public class Challenge03Sol {

    public static List<List<Integer>> solve(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int[] candidates, int remaining, int start,
                                  List<Integer> current, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;  // pruning
            current.add(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] candidates;
        if (line.isEmpty()) {
            candidates = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            candidates = new int[parts.length];
            for (int i = 0; i < parts.length; i++) candidates[i] = Integer.parseInt(parts[i]);
        }
        int target = Integer.parseInt(sc.nextLine().trim());
        List<List<Integer>> result = solve(candidates, target);
        for (List<Integer> combo : result) {
            System.out.println(combo);
        }
        sc.close();
    }
}
