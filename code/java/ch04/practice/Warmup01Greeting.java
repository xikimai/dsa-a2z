package ch04.practice;

import java.util.Scanner;

/**
 * Warmup 01: Greeting
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a function that takes a person's name and returns a greeting
 * string in the format "Hello, {name}!"
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a name (string, no spaces).
 *
 * OUTPUT FORMAT
 * -------------
 * Print the greeting string.
 *
 * CONSTRAINTS
 * -----------
 * name is a non-empty string of letters.
 *
 * EXAMPLES
 * --------
 * Input:  Maya
 * Output: Hello, Maya!
 *
 * Input:  World
 * Output: Hello, World!
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup01Greeting {

    /**
     * Return a greeting for the given name.
     *
     * @param name the person's name
     * @return "Hello, {name}!"
     */
    public static String solve(String name) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine().trim();
        System.out.println(solve(name));
        sc.close();
    }
}
