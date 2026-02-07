package ch08.learn;

/**
 * Example 01: Basic Sorts — Selection, Bubble, Insertion
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * This file demonstrates three fundamental O(n^2) sorting algorithms
 * with step-by-step visualizations so you can SEE how they work.
 *
 * Build and run:
 *   cd code/java
 *   javac ch08/learn/Example01BasicSorts.java
 *   java ch08.learn.Example01BasicSorts
 */
public class Example01BasicSorts {

    // ── Helper: print array ─────────────────────────────────────────
    static void printArray(int[] arr, String label) {
        StringBuilder sb = new StringBuilder("  " + label + " [");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(", ");
            sb.append(arr[i]);
        }
        sb.append("]");
        System.out.println(sb);
    }

    // ── 1. Selection Sort ───────────────────────────────────────────
    // Find the minimum, swap it to the front. Repeat.

    static int[] selectionSort(int[] arr) {
        int[] a = arr.clone();
        for (int i = 0; i < a.length; i++) {
            int minIdx = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIdx]) minIdx = j;
            }
            int temp = a[i];
            a[i] = a[minIdx];
            a[minIdx] = temp;
        }
        return a;
    }

    static void demoSelectionSort() {
        System.out.println("=== Part 1: Selection Sort ===");
        System.out.println("Idea: Find the smallest unsorted element, swap it into place.\n");

        int[] arr = {64, 25, 12, 22, 11};
        printArray(arr, "Start:  ");
        int[] a = arr.clone();
        for (int i = 0; i < a.length; i++) {
            int minIdx = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIdx]) minIdx = j;
            }
            System.out.printf("  Pass %d: min=%d at index %d, swap with index %d%n",
                i + 1, a[minIdx], minIdx, i);
            int temp = a[i];
            a[i] = a[minIdx];
            a[minIdx] = temp;
            printArray(a, "Result: ");
        }
        System.out.println("\n  Time: O(n^2) always | Space: O(1) | NOT stable\n");
    }

    // ── 2. Bubble Sort ──────────────────────────────────────────────
    // Repeatedly swap adjacent elements if they're in the wrong order.

    static int[] bubbleSort(int[] arr) {
        int[] a = arr.clone();
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return a;
    }

    static void demoBubbleSort() {
        System.out.println("=== Part 2: Bubble Sort ===");
        System.out.println("Idea: Bubble the largest element to the end, one pass at a time.\n");

        int[] arr = {5, 3, 8, 1, 2};
        printArray(arr, "Start:  ");
        int[] a = arr.clone();
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            int swapCount = 0;
            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                    swapped = true;
                    swapCount++;
                }
            }
            System.out.printf("  Pass %d: %d swap(s)", i + 1, swapCount);
            if (!swapped) {
                System.out.println(" -> no swaps, DONE early!");
                break;
            }
            printArray(a, " -> ");
        }
        System.out.println("\n  Time: O(n^2) worst, O(n) best (already sorted) | Space: O(1) | Stable\n");
    }

    // ── 3. Insertion Sort ───────────────────────────────────────────
    // Take each element and insert it into its correct position.

    static int[] insertionSort(int[] arr) {
        int[] a = arr.clone();
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
        return a;
    }

    static void demoInsertionSort() {
        System.out.println("=== Part 3: Insertion Sort ===");
        System.out.println("Idea: Pick each card and slide it into the right spot in the sorted hand.\n");

        int[] arr = {12, 11, 13, 5, 6};
        printArray(arr, "Start:  ");
        int[] a = arr.clone();
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            int shifts = 0;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
                shifts++;
            }
            a[j + 1] = key;
            System.out.printf("  Insert %d: shifted %d element(s), placed at index %d",
                key, shifts, j + 1);
            printArray(a, " -> ");
        }
        System.out.println("\n  Time: O(n^2) worst, O(n) best (already sorted) | Space: O(1) | Stable");
        System.out.println("  Fun fact: Insertion sort is often fastest for small arrays (n < 20)!\n");
    }

    // ── Comparison ──────────────────────────────────────────────────

    static void demoComparison() {
        System.out.println("=== Comparison of Basic Sorts ===\n");
        System.out.printf("  %-16s  %-12s  %-12s  %-8s  %s%n",
            "Algorithm", "Best", "Worst", "Space", "Stable?");
        System.out.println("  " + "-".repeat(60));
        System.out.printf("  %-16s  %-12s  %-12s  %-8s  %s%n",
            "Selection Sort", "O(n^2)", "O(n^2)", "O(1)", "No");
        System.out.printf("  %-16s  %-12s  %-12s  %-8s  %s%n",
            "Bubble Sort", "O(n)", "O(n^2)", "O(1)", "Yes");
        System.out.printf("  %-16s  %-12s  %-12s  %-8s  %s%n",
            "Insertion Sort", "O(n)", "O(n^2)", "O(1)", "Yes");
        System.out.println();
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 8: Basic Sorts — Selection, Bubble, Insertion");
        System.out.println("=====================================================\n");

        demoSelectionSort();
        demoBubbleSort();
        demoInsertionSort();
        demoComparison();

        System.out.println("KEY TAKEAWAY:");
        System.out.println("  All three are O(n^2) worst case, but each has a personality:");
        System.out.println("  - Selection: fewest swaps (good if swaps are expensive)");
        System.out.println("  - Bubble: can detect already-sorted input (best case O(n))");
        System.out.println("  - Insertion: best for nearly-sorted data and small arrays");
    }
}
