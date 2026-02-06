package ch03.learn;

/**
 * Example 02: Loops and Patterns
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * This file shows you how Java repeats work with for loops, while loops,
 * nested loops, break, continue, and some classic patterns.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch03/learn/Example02LoopsPatterns.java
 *   java ch03.learn.Example02LoopsPatterns
 */
public class Example02LoopsPatterns {

    public static void main(String[] args) {

        // ── 1. For Loop ────────────────────────────────────────────────
        System.out.println("=== For Loop ===");

        // Print numbers 1 to 5
        // for (init; condition; update)
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();  // newline after

        // Counting down
        System.out.print("Countdown: ");
        for (int i = 5; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();

        // ── 2. While Loop ─────────────────────────────────────────────
        System.out.println("=== While Loop ===");

        // Same thing with a while loop
        int count = 1;
        while (count <= 5) {
            System.out.print(count + " ");
            count++;
        }
        System.out.println();

        // do-while: runs at least once, then checks condition
        System.out.print("do-while: ");
        int x = 10;
        do {
            System.out.print(x + " ");
            x++;
        } while (x < 10);  // condition is false immediately, but body ran once!
        System.out.println("(body ran once even though 10 < 10 is false)");
        System.out.println();

        // ── 3. Break and Continue ──────────────────────────────────────
        System.out.println("=== Break and Continue ===");

        // break: exit the loop immediately
        System.out.print("Break at 4: ");
        for (int i = 1; i <= 10; i++) {
            if (i == 4) break;
            System.out.print(i + " ");
        }
        System.out.println();

        // continue: skip the rest of this iteration, go to the next
        System.out.print("Skip evens: ");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue;
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println();

        // ── 4. Nested Loops ───────────────────────────────────────────
        System.out.println("=== Nested Loops ===");

        // Multiplication table (3x3)
        System.out.println("3x3 Multiplication Table:");
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= 3; col++) {
                // printf lets you format output with fixed widths
                System.out.printf("%4d", row * col);
            }
            System.out.println();
        }
        System.out.println();

        // ── 5. Pattern: Right Triangle ─────────────────────────────────
        System.out.println("=== Pattern: Right Triangle (n=5) ===");

        int n = 5;
        for (int row = 1; row <= n; row++) {
            // Print stars: row 1 gets 1 star, row 2 gets 2, etc.
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();

        // ── 6. Pattern: Right-Aligned Triangle ─────────────────────────
        System.out.println("=== Pattern: Right-Aligned Triangle (n=5) ===");

        for (int row = 1; row <= n; row++) {
            // Print spaces first: row 1 needs (n-1) spaces, row 2 needs (n-2), etc.
            for (int s = 0; s < n - row; s++) {
                System.out.print(" ");
            }
            // Then stars
            for (int col = 0; col < row; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();

        // ── 7. Pattern: Number Triangle ────────────────────────────────
        System.out.println("=== Pattern: Number Triangle (n=5) ===");

        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print(col);
            }
            System.out.println();
        }
        System.out.println();

        // ── 8. Common Loop Patterns ────────────────────────────────────
        System.out.println("=== Sum of 1 to 10 ===");
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        System.out.println("Sum = " + sum + " (should be 55)");
        System.out.println();

        System.out.println("=== Finding Max in a Sequence ===");
        int[] numbers = {3, 7, 2, 9, 4, 1, 8};
        int max = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
        }
        System.out.println("Max = " + max + " (should be 9)");
    }
}
