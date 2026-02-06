package ch04.solutions;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/**
 * Solution for Challenge 02: Apply Operations
 * =============================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Process each operation name in order. For each operation, transform the
 * list accordingly:
 *   - "double":  multiply each element by 2
 *   - "negate":  multiply each element by -1
 *   - "sort":    sort ascending using Collections.sort
 *   - "reverse": reverse using Collections.reverse
 *   - "square":  replace each element with element * element
 * Ignore unknown operations.
 *
 * TIME COMPLEXITY:  O(m * n log n) worst case (m operations, n elements,
 *                   sort is the most expensive operation)
 * SPACE COMPLEXITY: O(n) for the working list
 */
public class Challenge02Sol {

    public static List<Integer> solve(List<Integer> nums, List<String> operations) {
        List<Integer> result = new ArrayList<>(nums);
        for (String op : operations) {
            switch (op) {
                case "double":
                    for (int i = 0; i < result.size(); i++) {
                        result.set(i, result.get(i) * 2);
                    }
                    break;
                case "negate":
                    for (int i = 0; i < result.size(); i++) {
                        result.set(i, result.get(i) * -1);
                    }
                    break;
                case "sort":
                    Collections.sort(result);
                    break;
                case "reverse":
                    Collections.reverse(result);
                    break;
                case "square":
                    for (int i = 0; i < result.size(); i++) {
                        result.set(i, result.get(i) * result.get(i));
                    }
                    break;
                default:
                    // ignore unknown operations
                    break;
            }
        }
        return result;
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
