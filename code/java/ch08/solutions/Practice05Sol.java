package ch08.solutions;

import java.util.*;

/**
 * Solution for Practice 05: Merge Two Sorted Arrays
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Two-pointer merge: maintain one pointer per array, always pick the
 * smaller element, then copy any remaining elements.
 *
 * TIME COMPLEXITY:  O(n + m)
 * SPACE COMPLEXITY: O(n + m)
 */
public class Practice05Sol {

    public static int[] solve(int[] arr1, int[] arr2) {
        int[] result = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) result[k++] = arr1[i++];
            else result[k++] = arr2[j++];
        }
        while (i < arr1.length) result[k++] = arr1[i++];
        while (j < arr2.length) result[k++] = arr2[j++];
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] arr1 = line1.isEmpty() ? new int[0] : Arrays.stream(line1.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] arr2 = line2.isEmpty() ? new int[0] : Arrays.stream(line2.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] result = solve(arr1, arr2);
        StringJoiner sj = new StringJoiner(" ");
        for (int v : result) sj.add(String.valueOf(v));
        System.out.println(sj);
        sc.close();
    }
}
