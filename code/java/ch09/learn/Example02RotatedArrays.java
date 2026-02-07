package ch09.learn;

/**
 * Example 02: Rotated Arrays — Search and Min-Finding
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * A rotated sorted array is a sorted array that has been "spun" at some
 * pivot point. For example, [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].
 *
 * This file demonstrates how binary search adapts to rotated arrays.
 *
 * Build and run:
 *   cd code/java
 *   javac ch09/learn/Example02RotatedArrays.java
 *   java ch09.learn.Example02RotatedArrays
 */
public class Example02RotatedArrays {

    // ── Helper ────────────────────────────────────────────────────────
    static void printArray(int[] arr, String label) {
        StringBuilder sb = new StringBuilder("  " + label + " [");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(", ");
            sb.append(arr[i]);
        }
        sb.append("]");
        System.out.println(sb);
    }

    // ── 1. What Is a Rotated Array? ──────────────────────────────────

    static void demoRotation() {
        System.out.println("=== Part 1: What Is a Rotated Sorted Array? ===\n");

        int[] original = {1, 2, 3, 4, 5, 6, 7};
        printArray(original, "Original sorted: ");
        System.out.println();

        for (int rot = 1; rot <= 6; rot++) {
            int[] rotated = new int[original.length];
            for (int i = 0; i < original.length; i++) {
                rotated[i] = original[(i + rot) % original.length];
            }
            printArray(rotated, "Rotated by " + rot + ":   ");
        }

        System.out.println();
        System.out.println("  Key insight: A rotated sorted array has TWO sorted halves.");
        System.out.println("  There's exactly one \"break point\" where the big-to-small jump happens.\n");
    }

    // ── 2. Finding the Minimum (the Pivot) ───────────────────────────

    static int findMin(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > arr[hi]) lo = mid + 1;
            else hi = mid;
        }
        return arr[lo];
    }

    static void demoFindMin() {
        System.out.println("=== Part 2: Finding the Minimum in a Rotated Array ===\n");

        int[] arr = {4, 5, 6, 7, 0, 1, 2};
        printArray(arr, "Array:  ");
        System.out.println();

        int lo = 0, hi = arr.length - 1;
        int steps = 0;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            steps++;
            System.out.printf("  Step %d: lo=%d(%d), hi=%d(%d), mid=%d(%d)",
                steps, lo, arr[lo], hi, arr[hi], mid, arr[mid]);
            if (arr[mid] > arr[hi]) {
                System.out.println(" -> mid > hi, min is RIGHT of mid");
                lo = mid + 1;
            } else {
                System.out.println(" -> mid <= hi, min is at mid or LEFT");
                hi = mid;
            }
        }
        System.out.println("  Answer: min = " + arr[lo] + " at index " + lo);
        System.out.println("  Steps: " + steps + " (O(log n))\n");
    }

    // ── 3. Searching in a Rotated Array ──────────────────────────────

    static int searchRotated(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return mid;
            if (arr[lo] <= arr[mid]) {
                if (arr[lo] <= target && target < arr[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else {
                if (arr[mid] < target && target <= arr[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }

    static void demoSearchRotated() {
        System.out.println("=== Part 3: Searching in a Rotated Array ===\n");

        int[] arr = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        printArray(arr, "Array:  ");
        System.out.println("  Target: " + target + "\n");

        int lo = 0, hi = arr.length - 1;
        int steps = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            steps++;
            System.out.printf("  Step %d: lo=%d(%d), hi=%d(%d), mid=%d(%d)",
                steps, lo, arr[lo], hi, arr[hi], mid, arr[mid]);
            if (arr[mid] == target) {
                System.out.println(" FOUND!");
                break;
            }
            if (arr[lo] <= arr[mid]) {
                if (arr[lo] <= target && target < arr[mid]) {
                    System.out.println(" -> left half sorted & target in left");
                    hi = mid - 1;
                } else {
                    System.out.println(" -> left half sorted but target NOT in left");
                    lo = mid + 1;
                }
            } else {
                if (arr[mid] < target && target <= arr[hi]) {
                    System.out.println(" -> right half sorted & target in right");
                    lo = mid + 1;
                } else {
                    System.out.println(" -> right half sorted but target NOT in right");
                    hi = mid - 1;
                }
            }
        }
        System.out.println("  Steps: " + steps + "\n");
    }

    // ── 4. Finding a Peak Element ────────────────────────────────────

    static int findPeak(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static void demoPeakElement() {
        System.out.println("=== Part 4: Finding a Peak Element ===\n");
        System.out.println("  A peak is an element greater than both its neighbors.");
        System.out.println("  (Boundaries count as -infinity.)\n");

        int[] arr = {1, 2, 1, 3, 5, 6, 4};
        printArray(arr, "Array:  ");
        System.out.println();

        int lo = 0, hi = arr.length - 1;
        int steps = 0;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            steps++;
            System.out.printf("  Step %d: lo=%d, hi=%d, mid=%d -> arr[%d]=%d, arr[%d]=%d",
                steps, lo, hi, mid, mid, arr[mid], mid + 1, arr[mid + 1]);
            if (arr[mid] < arr[mid + 1]) {
                System.out.println(" -> climbing up, peak is RIGHT");
                lo = mid + 1;
            } else {
                System.out.println(" -> going down, peak is at mid or LEFT");
                hi = mid;
            }
        }
        System.out.println("  Peak found at index " + lo + ", value = " + arr[lo]);
        System.out.println("  Steps: " + steps + "\n");
    }

    // ── Main ──────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 9: Rotated Arrays and Beyond");
        System.out.println("=====================================\n");

        demoRotation();
        demoFindMin();
        demoSearchRotated();
        demoPeakElement();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Rotated sorted arrays still have structure we can exploit");
        System.out.println("  2. The trick: figure out which HALF is sorted, then decide");
        System.out.println("  3. Peak finding: always climb uphill — O(log n)");
        System.out.println("  4. Binary search is not just for sorted arrays!");
    }
}
