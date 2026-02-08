package ch16.learn;

/**
 * Example 01: Binary Search on Answers Basics
 * =============================================
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * Demonstrates BS on answers for integer square root and Koko's bananas.
 */
public class Example01BsOnAnswersBasics {

    public static void main(String[] args) {
        // Part 1: Integer Square Root
        System.out.println("=== Part 1: BS on Answers — Integer Square Root ===");
        int n = 49;
        System.out.println("Finding floor(sqrt(" + n + "))");

        int lo = 0, hi = n;
        int step = 0;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            step++;
            long sq = (long) mid * mid;
            System.out.printf("  Step %d: mid=%d, mid*mid=%d", step, mid, sq);
            if (sq <= n) {
                System.out.println(" <= " + n + " -> lo = " + mid);
                lo = mid;
            } else {
                System.out.println(" > " + n + " -> hi = " + (mid - 1));
                hi = mid - 1;
            }
        }
        System.out.println("Answer: floor(sqrt(" + n + ")) = " + lo);

        // Part 2: Koko's Bananas
        System.out.println("\n=== Part 2: BS on Answers — Koko Eating Bananas ===");
        int[] piles = {3, 6, 7, 11};
        int h = 8;
        System.out.print("Piles: [");
        for (int i = 0; i < piles.length; i++) {
            System.out.print(piles[i] + (i < piles.length - 1 ? ", " : ""));
        }
        System.out.println("], Hours: " + h);

        int maxPile = 0;
        for (int p : piles) maxPile = Math.max(maxPile, p);

        lo = 1;
        hi = maxPile;
        step = 0;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            step++;
            int hours = 0;
            for (int p : piles) hours += (p + mid - 1) / mid;
            System.out.printf("  Step %d: speed=%d, hours=%d", step, mid, hours);
            if (hours <= h) {
                System.out.println(" <= " + h + " -> hi = " + mid);
                hi = mid;
            } else {
                System.out.println(" > " + h + " -> lo = " + (mid + 1));
                lo = mid + 1;
            }
        }
        System.out.println("Minimum eating speed: " + lo);
    }
}
