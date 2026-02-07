package ch08.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Dutch National Flag
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three-pointer technique (Dijkstra's Dutch National Flag):
 *   lo  = boundary for 0s (everything before lo is 0)
 *   mid = current element being examined
 *   hi  = boundary for 2s (everything after hi is 2)
 *
 * Walk mid from left to right:
 *   - If arr[mid] == 0: swap with arr[lo], advance both lo and mid
 *   - If arr[mid] == 1: just advance mid
 *   - If arr[mid] == 2: swap with arr[hi], decrement hi (don't advance mid)
 *
 * TIME COMPLEXITY:  O(n) single pass
 * SPACE COMPLEXITY: O(1)
 */
public class Practice03Sol {

    public static int[] solve(int[] arr) {
        int[] a = arr.clone();
        int lo = 0, mid = 0, hi = a.length - 1;
        while (mid <= hi) {
            if (a[mid] == 0) {
                int temp = a[lo];
                a[lo] = a[mid];
                a[mid] = temp;
                lo++;
                mid++;
            } else if (a[mid] == 1) {
                mid++;
            } else {
                int temp = a[mid];
                a[mid] = a[hi];
                a[hi] = temp;
                hi--;
            }
        }
        return a;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println();
        } else {
            String[] parts = line.split("\\s+");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            int[] result = solve(arr);
            StringJoiner sj = new StringJoiner(" ");
            for (int v : result) sj.add(String.valueOf(v));
            System.out.println(sj);
        }
        sc.close();
    }
}
