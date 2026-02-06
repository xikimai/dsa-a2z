package ch05.solutions;

import java.util.*;

/**
 * Solution for Warmup 01: Second Largest
 * =======================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Single pass: track the largest and second largest as we scan.
 * Initialize both to Integer.MIN_VALUE. For each element:
 *   - If it's bigger than first, second = first, first = element
 *   - Else if it's bigger than second AND not equal to first, second = element
 * If second is still Integer.MIN_VALUE at the end, return -1.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup01Sol {

    public static int solve(int[] nums) {
        if (nums.length < 2) return -1;

        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;

        for (int n : nums) {
            if (n > first) {
                second = first;
                first = n;
            } else if (n > second && n != first) {
                second = n;
            }
        }

        return (second == Integer.MIN_VALUE) ? -1 : second;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            int[] nums = Arrays.stream(line.split("\\s+"))
                               .mapToInt(Integer::parseInt).toArray();
            System.out.println(solve(nums));
        }
        sc.close();
    }
}
