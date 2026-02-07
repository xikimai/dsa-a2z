package ch09.learn;

/**
 * Example 01: Binary Search — Visual Comparison
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * This file demonstrates why binary search is so much faster than
 * linear search, with step-by-step traces you can follow.
 *
 * Build and run:
 *   cd code/java
 *   javac ch09/learn/Example01BinarySearchVisual.java
 *   java ch09.learn.Example01BinarySearchVisual
 */
public class Example01BinarySearchVisual {

    // ── Helper: print array with pointer ──────────────────────────────
    static void printArrayWithPointer(int[] arr, int idx, String label) {
        StringBuilder sb = new StringBuilder("  " + label + " [");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(", ");
            if (i == idx) sb.append(">>").append(arr[i]).append("<<");
            else sb.append(arr[i]);
        }
        sb.append("]");
        System.out.println(sb);
    }

    static void printArray(int[] arr, String label) {
        StringBuilder sb = new StringBuilder("  " + label + " [");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(", ");
            sb.append(arr[i]);
        }
        sb.append("]");
        System.out.println(sb);
    }

    // ── 1. Linear Search ──────────────────────────────────────────────
    // Check every element one by one. Simple but slow.

    static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }

    static void demoLinearSearch() {
        System.out.println("=== Part 1: Linear Search ===");
        System.out.println("Idea: Check every element, left to right, until you find it.\n");

        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        printArray(arr, "Array:  ");
        System.out.println("  Target: " + target + "\n");

        int steps = 0;
        for (int i = 0; i < arr.length; i++) {
            steps++;
            System.out.printf("  Step %d: check index %d -> arr[%d] = %d", steps, i, i, arr[i]);
            if (arr[i] == target) {
                System.out.println(" FOUND!");
                break;
            }
            System.out.println(" (not it)");
        }
        System.out.println("  Total steps: " + steps);
        System.out.println("\n  Time: O(n) — must check up to every element\n");
    }

    // ── 2. Binary Search ──────────────────────────────────────────────
    // Cut the search space in half each time. Requires sorted array.

    static int binarySearch(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    static void demoBinarySearch() {
        System.out.println("=== Part 2: Binary Search (Step-by-Step Trace) ===");
        System.out.println("Idea: Look at the middle element. If too small, search right half.");
        System.out.println("      If too big, search left half. Repeat.\n");

        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        printArray(arr, "Array:  ");
        System.out.println("  Target: " + target + "\n");

        int lo = 0, hi = arr.length - 1;
        int steps = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            steps++;
            System.out.printf("  Step %d: lo=%d, hi=%d, mid=%d -> arr[%d] = %d",
                steps, lo, hi, mid, mid, arr[mid]);
            if (arr[mid] == target) {
                System.out.println(" FOUND!");
                break;
            } else if (arr[mid] < target) {
                System.out.println(" (too small, search RIGHT)");
                lo = mid + 1;
            } else {
                System.out.println(" (too big, search LEFT)");
                hi = mid - 1;
            }
        }
        System.out.println("  Total steps: " + steps);
        System.out.println("\n  Time: O(log n) — halving the range each time\n");
    }

    // ── 3. Step Count Comparison ──────────────────────────────────────

    static void demoComparison() {
        System.out.println("=== Part 3: Step Count Comparison ===\n");

        int[] sizes = {10, 100, 1000, 10000, 100000, 1000000};
        System.out.printf("  %-12s  %-14s  %-14s%n", "Array Size", "Linear (worst)", "Binary (worst)");
        System.out.println("  " + "-".repeat(44));
        for (int n : sizes) {
            int linearSteps = n;
            int binarySteps = 0;
            int temp = n;
            while (temp > 0) {
                binarySteps++;
                temp /= 2;
            }
            System.out.printf("  %-12d  %-14d  %-14d%n", n, linearSteps, binarySteps);
        }
        System.out.println();
        System.out.println("  Notice: When the array has 1,000,000 elements:");
        System.out.println("    - Linear search: up to 1,000,000 steps");
        System.out.println("    - Binary search: at most 20 steps!");
        System.out.println();
    }

    // ── 4. Searching for missing elements ─────────────────────────────

    static void demoNotFound() {
        System.out.println("=== Part 4: When the Target Is NOT There ===\n");

        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 25;
        printArray(arr, "Array:  ");
        System.out.println("  Target: " + target + " (not in array)\n");

        int lo = 0, hi = arr.length - 1;
        int steps = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            steps++;
            System.out.printf("  Step %d: lo=%d, hi=%d, mid=%d -> arr[%d] = %d",
                steps, lo, hi, mid, mid, arr[mid]);
            if (arr[mid] == target) {
                System.out.println(" FOUND!");
                break;
            } else if (arr[mid] < target) {
                System.out.println(" (too small, search RIGHT)");
                lo = mid + 1;
            } else {
                System.out.println(" (too big, search LEFT)");
                hi = mid - 1;
            }
        }
        if (lo > hi) {
            System.out.println("  lo > hi -> NOT FOUND (returned -1)");
        }
        System.out.println("  Total steps: " + steps + " (still fast even when not found!)\n");
    }

    // ── Main ──────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 9: Binary Search — Visual Comparison");
        System.out.println("=============================================\n");

        demoLinearSearch();
        demoBinarySearch();
        demoComparison();
        demoNotFound();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Linear search: O(n) — works on ANY array, sorted or not");
        System.out.println("  2. Binary search: O(log n) — ONLY works on sorted arrays");
        System.out.println("  3. Always use `mid = lo + (hi - lo) / 2` to avoid overflow");
        System.out.println("  4. Binary search is a superpower — learn it well!");
    }
}
