package ch10.solutions;

import java.util.*;

/**
 * Solution for Practice 05: Generate All Subsets
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort input first. Backtracking: at each element, include or exclude.
 *           Sort result by size then lexicographically.
 *
 * TIME COMPLEXITY:  O(2^n * n) — 2^n subsets, each up to length n
 * SPACE COMPLEXITY: O(2^n * n) — storing all subsets
 */
public class Practice05Sol {

    public static List<List<Integer>> solve(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        result.sort((a, b) -> {
            if (a.size() != b.size()) return a.size() - b.size();
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }

    private static void backtrack(int[] nums, int idx, List<Integer> current,
                                  List<List<Integer>> result) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        // Exclude
        backtrack(nums, idx + 1, current, result);
        // Include
        current.add(nums[idx]);
        backtrack(nums, idx + 1, current, result);
        current.remove(current.size() - 1);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] nums;
        if (line.isEmpty()) {
            nums = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        }
        List<List<Integer>> result = solve(nums);
        for (List<Integer> subset : result) {
            System.out.println(subset);
        }
        sc.close();
    }
}
