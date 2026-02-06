package ch05.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Sort by Frequency
 * =============================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * 1. Count frequencies using a HashMap.
 * 2. Box the array into Integer[] so we can use a custom Comparator.
 * 3. Sort with comparator: higher frequency first; if tied, smaller value first.
 * 4. Unbox back to int[].
 *
 * TIME COMPLEXITY:  O(n log n) for sorting
 * SPACE COMPLEXITY: O(n) for the frequency map and boxed array
 */
public class Practice04Sol {

    public static int[] solve(int[] nums) {
        // Count frequencies
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }

        // Box to Integer[] for custom sort
        Integer[] boxed = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            boxed[i] = nums[i];
        }

        // Sort: higher frequency first, then smaller value first
        Arrays.sort(boxed, (a, b) -> {
            int freqDiff = freq.get(b) - freq.get(a);
            if (freqDiff != 0) return freqDiff;
            return a - b;
        });

        // Unbox back to int[]
        int[] result = new int[nums.length];
        for (int i = 0; i < boxed.length; i++) {
            result[i] = boxed[i];
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                           .mapToInt(Integer::parseInt).toArray();
        int[] result = solve(nums);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
