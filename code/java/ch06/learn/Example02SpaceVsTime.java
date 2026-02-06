package ch06.learn;

import java.util.*;

/**
 * Example 02: Space vs Time Tradeoff
 * ===================================
 * Chapter 6: How Fast Is Your Code?
 *
 * The same problem — "contains duplicate" — solved three ways.
 * Each approach trades space for speed differently.
 *
 * Build and run:
 *   cd code/java
 *   javac ch06/learn/Example02SpaceVsTime.java
 *   java ch06.learn.Example02SpaceVsTime
 */
public class Example02SpaceVsTime {

    // ── Part 1: O(n^2) Brute Force — No Extra Space ─────────────────
    // Compare every pair. Slow but uses O(1) extra memory.

    static boolean containsDupBrute(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) return true;
            }
        }
        return false;
    }

    static void demoBrute() {
        System.out.println("=== Part 1: O(n^2) Brute Force ===");
        System.out.println("Compare every pair — no extra memory needed.");
        System.out.println();

        int[] example = {3, 1, 4, 1, 5, 9};
        System.out.println("  Input:  " + Arrays.toString(example));
        System.out.println("  Result: " + containsDupBrute(example));
        System.out.println("  Time:  O(n^2)   Space: O(1)");
        System.out.println();
    }

    // ── Part 2: O(n log n) Sort — Clever Middle Ground ──────────────
    // Sort first, then check neighbors. Modifies the array.

    static boolean containsDupSort(int[] nums) {
        int[] sorted = nums.clone();  // don't destroy original
        Arrays.sort(sorted);
        for (int i = 1; i < sorted.length; i++) {
            if (sorted[i] == sorted[i - 1]) return true;
        }
        return false;
    }

    static void demoSort() {
        System.out.println("=== Part 2: O(n log n) Sort ===");
        System.out.println("Sort, then check adjacent elements.");
        System.out.println();

        int[] example = {3, 1, 4, 1, 5, 9};
        System.out.println("  Input:  " + Arrays.toString(example));
        System.out.println("  Sorted: " + Arrays.toString(
            Arrays.stream(example).sorted().toArray()));
        System.out.println("  Result: " + containsDupSort(example));
        System.out.println("  Time:  O(n log n)   Space: O(n) for clone");
        System.out.println();
    }

    // ── Part 3: O(n) HashSet — Trade Space for Speed ────────────────
    // Use a set to remember what we've seen. Fastest!

    static boolean containsDupHash(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) return true;  // add returns false if already present
        }
        return false;
    }

    static void demoHash() {
        System.out.println("=== Part 3: O(n) HashSet ===");
        System.out.println("Track seen elements — fastest approach.");
        System.out.println();

        int[] example = {3, 1, 4, 1, 5, 9};
        System.out.println("  Input:  " + Arrays.toString(example));
        System.out.println("  Result: " + containsDupHash(example));
        System.out.println("  Time:  O(n)   Space: O(n)");
        System.out.println();
    }

    // ── Part 4: Timing Comparison ───────────────────────────────────

    static void demoTiming() {
        System.out.println("=== Part 4: Timing Comparison ===");
        System.out.println("Let's race all three on the same data!\n");

        int[] sizes = {1_000, 5_000, 10_000};

        for (int size : sizes) {
            // Create array with one duplicate at the end
            int[] data = new int[size];
            for (int i = 0; i < size - 1; i++) data[i] = i;
            data[size - 1] = 0;  // duplicate of first element

            // Brute force
            long start = System.nanoTime();
            containsDupBrute(data);
            long bruteTime = System.nanoTime() - start;

            // Sort
            start = System.nanoTime();
            containsDupSort(data);
            long sortTime = System.nanoTime() - start;

            // Hash
            start = System.nanoTime();
            containsDupHash(data);
            long hashTime = System.nanoTime() - start;

            System.out.printf("  n = %,6d:%n", size);
            System.out.printf("    Brute O(n^2):     %,10d ns%n", bruteTime);
            System.out.printf("    Sort  O(n log n): %,10d ns%n", sortTime);
            System.out.printf("    Hash  O(n):       %,10d ns%n", hashTime);
            System.out.println();
        }

        System.out.println("  The HashSet approach wins — we traded extra memory");
        System.out.println("  for much faster execution. That's the space-time tradeoff!");
    }

    // ── Summary Table ───────────────────────────────────────────────

    static void printSummary() {
        System.out.println("=== Summary: Space vs Time ===");
        System.out.println();
        System.out.println("  Approach      | Time       | Space  | When to use");
        System.out.println("  ------------- | ---------- | ------ | --------------------------");
        System.out.println("  Brute force   | O(n^2)     | O(1)   | Tiny n, memory-constrained");
        System.out.println("  Sort first    | O(n log n) | O(n)   | Need sorted order anyway");
        System.out.println("  HashSet       | O(n)       | O(n)   | Best general-purpose");
        System.out.println();
    }

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 6: Space vs Time Tradeoff");
        System.out.println("=================================\n");

        demoBrute();
        demoSort();
        demoHash();
        demoTiming();
        printSummary();
    }
}
