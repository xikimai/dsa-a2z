package ch05.solutions;

import java.util.*;

/**
 * Solution for Challenge 01: Find Duplicates (Three Ways)
 * ========================================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three approaches implemented:
 *   solveBrute — O(n^2) nested loops checking each pair
 *   solveSort  — O(n log n) sort, then scan adjacent elements
 *   solveSet   — O(n) using a HashSet (seen) and a TreeSet (duplicates)
 *
 * solve() uses the set approach for best performance.
 *
 * TIME COMPLEXITY:  O(n) for solve/solveSet
 * SPACE COMPLEXITY: O(n) for the sets
 */
public class Challenge01Sol {

    public static int[] solveBrute(int[] nums) {
        TreeSet<Integer> dups = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    dups.add(nums[i]);
                }
            }
        }
        return dups.stream().mapToInt(Integer::intValue).toArray();
    }

    public static int[] solveSort(int[] nums) {
        if (nums.length < 2) return new int[0];
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        TreeSet<Integer> dups = new TreeSet<>();
        for (int i = 1; i < sorted.length; i++) {
            if (sorted[i] == sorted[i - 1]) {
                dups.add(sorted[i]);
            }
        }
        return dups.stream().mapToInt(Integer::intValue).toArray();
    }

    public static int[] solveSet(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        TreeSet<Integer> dups = new TreeSet<>();
        for (int n : nums) {
            if (!seen.add(n)) {
                dups.add(n);
            }
        }
        return dups.stream().mapToInt(Integer::intValue).toArray();
    }

    public static int[] solve(int[] nums) {
        return solveSet(nums);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] nums;
        if (line.isEmpty()) {
            nums = new int[0];
        } else {
            nums = Arrays.stream(line.split("\\s+"))
                         .mapToInt(Integer::parseInt).toArray();
        }
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
