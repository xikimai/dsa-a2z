package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 01: Greeting
 * =================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Concatenate "Hello, " + name + "!" using string concatenation.
 * Java makes this easy with the + operator on strings.
 *
 * TIME COMPLEXITY:  O(n) — where n is the length of the name (string concat)
 * SPACE COMPLEXITY: O(n) — the new string takes space proportional to name length
 */
public class Warmup01Sol {

    /**
     * Return a greeting for the given name.
     *
     * @param name the person's name
     * @return a string in the format "Hello, <name>!"
     */
    public static String solve(String name) {
        return "Hello, " + name + "!";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        System.out.println(solve(name));
        scanner.close();
    }
}
