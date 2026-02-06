package ch06.solutions;

import java.util.*;

/**
 * Solution for Challenge 01: Two Sum — Three Ways
 * =================================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three approaches to the same problem:
 *   1. Brute force O(n^2): try every pair
 *   2. Sort O(n log n): pair values with original indices, sort, two-pointer
 *   3. Hash O(n): use a HashMap to find complements
 *
 * All return {i, j} with i < j, or {-1, -1} if no solution.
 */
public class Challenge01Sol {

    public static int[] solveBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }

    public static int[] solveSort(int[] nums, int target) {
        int n = nums.length;
        int[][] indexed = new int[n][2];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = nums[i];
            indexed[i][1] = i;
        }
        Arrays.sort(indexed, (a, b) -> Integer.compare(a[0], b[0]));

        int left = 0, right = n - 1;
        while (left < right) {
            int sum = indexed[left][0] + indexed[right][0];
            if (sum == target) {
                int i = Math.min(indexed[left][1], indexed[right][1]);
                int j = Math.max(indexed[left][1], indexed[right][1]);
                return new int[]{i, j};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }

    public static int[] solveHash(int[] nums, int target) {
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

    public static int[] solve(int[] nums, int target) {
        return solveHash(nums, target);
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
