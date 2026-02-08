package ch10.solutions;

import java.util.*;

/**
 * Solution for Challenge 02: Generate All Permutations
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort input. Backtracking: at each position, try every unused
 *           element. The sorted input ensures lexicographic order.
 *
 * TIME COMPLEXITY:  O(n! * n)
 * SPACE COMPLEXITY: O(n! * n) — storing all permutations
 */
public class Challenge02Sol {

    public static List<List<Integer>> solve(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int[] nums, boolean[] used, List<Integer> current,
                                  List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
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
        for (List<Integer> perm : result) {
            System.out.println(perm);
        }
        sc.close();
    }
}
