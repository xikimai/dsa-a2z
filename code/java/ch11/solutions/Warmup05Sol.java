package ch11.solutions;

import java.util.*;

/**
 * Solution for Warmup 5: Intersection of Two Arrays
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Put all elements of array a into a HashSet, then iterate through
 *           array b and collect elements that exist in the set.
 *           Use a second set to avoid duplicates. Sort the result.
 * TIME:  O(n + m + k log k) where k = size of intersection
 * SPACE: O(n + m)
 */
public class Warmup05Sol {
    public static List<Integer> solve(int[] a, int[] b) {
        HashSet<Integer> setA = new HashSet<>();
        for (int x : a) setA.add(x);

        HashSet<Integer> common = new HashSet<>();
        for (int x : b) {
            if (setA.contains(x)) {
                common.add(x);
            }
        }

        List<Integer> result = new ArrayList<>(common);
        Collections.sort(result);
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int m = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++) b[i] = sc.nextInt();
        System.out.println(solve(a, b));
        sc.close();
    }
}
