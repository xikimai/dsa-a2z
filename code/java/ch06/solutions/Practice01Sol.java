package ch06.solutions;

import java.util.*;

/**
 * Solution for Practice 01: Contains Duplicate
 * ==============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a HashSet. For each element, try to add it. If add() returns false,
 * we've seen it before -> duplicate found!
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n)
 */
public class Practice01Sol {

    public static boolean solve(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) return true;
        }
        return false;
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
