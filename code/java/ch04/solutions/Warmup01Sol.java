package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 01: Greeting
 * =================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Simple string concatenation: "Hello, " + name + "!"
 *
 * TIME COMPLEXITY:  O(n) where n is the length of the name
 * SPACE COMPLEXITY: O(n) for the new string
 */
public class Warmup01Sol {

    public static String solve(String name) {
        return "Hello, " + name + "!";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine().trim();
        System.out.println(solve(name));
        sc.close();
    }
}
