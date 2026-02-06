package ch05.solutions;

import java.util.*;

/**
 * Solution for Practice 01: Union of Two Arrays
 * ===============================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Add all elements from both arrays into a HashSet (removes duplicates),
 * convert to a list, sort, and convert to int[].
 *
 * TIME COMPLEXITY:  O((n+m) log(n+m)) due to sorting
 * SPACE COMPLEXITY: O(n+m) for the set
 */
public class Practice01Sol {

    public static int[] solve(int[] a, int[] b) {
        HashSet<Integer> set = new HashSet<>();
        for (int n : a) set.add(n);
        for (int n : b) set.add(n);

        int[] result = new int[set.size()];
        int i = 0;
        for (int n : set) {
            result[i++] = n;
        }
        Arrays.sort(result);
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] a = line1.isEmpty() ? new int[0]
            : Arrays.stream(line1.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] b = line2.isEmpty() ? new int[0]
            : Arrays.stream(line2.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] result = solve(a, b);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
