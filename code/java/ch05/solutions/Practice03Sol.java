package ch05.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Two Sum
 * ===================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * HashMap complement lookup: for each element, check if (target - element)
 * is already in the map. If yes, we found our pair. If not, store the
 * current element's index in the map.
 *
 * TIME COMPLEXITY:  O(n) — single pass
 * SPACE COMPLEXITY: O(n) for the hash map
 */
public class Practice03Sol {

    public static int[] solve(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                           .mapToInt(Integer::parseInt).toArray();
        int target = Integer.parseInt(sc.nextLine().trim());
        int[] result = solve(nums, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
