package ch04.practice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/**
 * Challenge 02: Apply Operations
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Given a list of integers and a list of operation names, apply each
 * operation to the list in order and return the final result.
 *
 * Supported operations:
 *   "double"  — multiply every element by 2
 *   "negate"  — multiply every element by -1
 *   "sort"    — sort in ascending order
 *   "reverse" — reverse the list
 *   "square"  — replace each element with its square
 *
 * Ignore any unknown operation names.
 *
 * INPUT FORMAT
 * ------------
 * Line 1: n (number of integers)
 * Line 2: n space-separated integers
 * Line 3: m (number of operations)
 * Line 4: m space-separated operation names
 *
 * OUTPUT FORMAT
 * -------------
 * Print the final list, elements separated by spaces.
 *
 * EXAMPLES
 * --------
 * Input:  3
 *         3 1 2
 *         2
 *         sort double
 * Output: 2 4 6
 *
 * Input:  4
 *         5 -3 7 1
 *         3
 *         negate sort reverse
 * Output: 3 -1 -5 -7
 *
 * INSTRUCTIONS
 * ------------
 * 1. Write helper functions for each operation (or handle inline).
 * 2. Process operations in order.
 * 3. Return empty list as default.
 * The main method handles input/output -- don't change it.
 */
public class Challenge02ApplyOperations {

    /**
     * Apply a sequence of operations to a list of integers.
     *
     * @param nums       the list of integers
     * @param operations the list of operation names to apply in order
     * @return the transformed list
     */
    public static List<Integer> solve(List<Integer> nums, List<String> operations) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String[] numParts = sc.nextLine().trim().split(" ");
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(numParts[i]));
        }
        int m = Integer.parseInt(sc.nextLine().trim());
        String[] opParts = sc.nextLine().trim().split(" ");
        List<String> operations = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            operations.add(opParts[i]);
        }
        List<Integer> result = solve(nums, operations);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(result.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
